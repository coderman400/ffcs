from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image, ImageEnhance
import textwrap
import os
import json
from pathlib import Path
import cv2
import numpy as np

TEMPLATE_IMAGE = Path("./assets/template.jpg")
OUTPUT_DIR = Path("./outputs")
INBETWEENS = Path("./assets/inbetweens")
HIGH_CONTRAST_FACTOR = 2.0

class TextExtraction:
    def __init__(self, image_path: str):
        self.image_path = Path(image_path)
        self.image = cv2.imread(str(self.image_path))
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.height, self.width = self.image.shape[:2]
        self.template = cv2.imread(str(TEMPLATE_IMAGE), 0)
        self.matched_crop = self.template_matching()
        self.contoured, self.contoured_path = self.contour_matching()
        self.optimized = self.increase_contrast()

        self.setup_genai()
        self.text = self.extract()
        self.post_process()
        self.clean_up()

    def setup_genai(self):
        """Setup GenAI with API key and configuration."""
        load_dotenv()
        genai.configure(api_key=os.getenv("api_key"))
        self.genai_image = genai.upload_file(self.optimized)
        self.model = genai.GenerativeModel("gemini-1.5-pro-latest", tools=self.tools())

    def template_matching(self):
        """Perform template matching to find the crop area."""
        result = cv2.matchTemplate(self.gray, self.template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        template_h, template_w = self.template.shape[:2]
        top_left = max_loc
        bottom_right = (top_left[0] + template_w, self.height - 1)
        matched_crop = self.image[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
        return matched_crop

    def contour_matching(self):
        """Find and save contours in the cropped image."""
        gray = cv2.cvtColor(self.matched_crop, cv2.COLOR_BGR2GRAY)
        thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 2)
        horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (40, 1))
        horizontal_lines = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)
        contours, _ = cv2.findContours(horizontal_lines, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        greater = []
        height, width = self.matched_crop.shape[:2]

        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            if w == width:
                greater.append((x, y))

        contoured = self.matched_crop[0:max(greater)[1], 0:self.width]
        contoured_path = INBETWEENS/ "contoured.jpg"
        cv2.imwrite(str(contoured_path), contoured)
        print(contoured_path)
        return contoured, str(contoured_path)

    def increase_contrast(self):
        """Enhance the contrast of the contoured image."""
        image = Image.open(self.contoured_path)
        image = image.convert('L')
        enhancer = ImageEnhance.Contrast(image)
        enhanced_image = enhancer.enhance(HIGH_CONTRAST_FACTOR)
        output_path = INBETWEENS / "high_contrast_image.png"
        enhanced_image.save(str(output_path))
        print(output_path)
        return str(output_path)

    def extract(self):
        """Extract text from the image using GenAI."""
        result = self.model.generate_content([   
            self.genai_image,
            "Extract information from the image"],
            tool_config={'function_calling_config': 'ANY'}
        )
        fc = result.candidates[0].content.parts[0].function_call
        data = type(fc).to_dict(fc)
        
        return data["args"]
    
    def printable(self) -> str:
        """Return the extracted text as a formatted JSON string."""
        return json.dumps(self.text, indent=4)

    def tools(self):
        """Define the tools schema for GenAI."""
        slot = genai.protos.Schema(
            type=genai.protos.Type.OBJECT,
            properties={
                'faculty': genai.protos.Schema(type=genai.protos.Type.STRING),
                'slot': genai.protos.Schema(type=genai.protos.Type.STRING),
                'venue': genai.protos.Schema(type=genai.protos.Type.STRING),
                'course_type': genai.protos.Schema(type=genai.protos.Type.STRING),
            },
            required=['faculty', 'slot', 'venue', 'course_type']
        )

        slots = genai.protos.Schema(
            type=genai.protos.Type.ARRAY,
            items=slot
        )

        course = genai.protos.Schema(
            type=genai.protos.Type.OBJECT,
            properties={
                'course_list': genai.protos.Schema(type=genai.protos.Type.STRING),
                'semester': genai.protos.Schema(type=genai.protos.Type.STRING),
                'curriculum_category': genai.protos.Schema(type=genai.protos.Type.STRING),
            },
        )

        extract = genai.protos.FunctionDeclaration(
            name="add_to_database",
            description=textwrap.dedent("""\
                Adds entities to the database.
                """),
            parameters=genai.protos.Schema(
                type=genai.protos.Type.OBJECT,
                properties={
                    'course': course,
                    'slots': slots
                }
            )
        )

        return [extract]

    def post_process(self):
        """Post-process the extracted text."""
        data = self.text
        for slot in data['slots']:
            slot['prof'] = slot.pop('faculty')
            slot['slots'] = slot.pop('slot')
        
        code,title = data['course']['course_list'].split("-",1)
        data['title'] = title.strip()
        data['code'] = code.strip()
        if "semester" in data.keys() and "course" in data.keys():
            data['semester'] = data['course']['semester']   
            data['category'] = data['course']['curriculum_category']
        del data['course']

        profs = set()
        for slot in data['slots']:
            profs.add(slot['prof'])
        
        data["slots_new"] = []

        for prof in profs:
            prof_slots = []
            for slot in data['slots']:
                if slot['prof'] == prof:
                    prof_slots.append(slot["slots"])
            data["slots_new"].append({"prof": prof, "slots": ",".join(prof_slots)})

        data["slots"] = data.pop("slots_new")
        self.text = data

    def write(self):
        """Write the extracted text to a JSON file."""
        output_path = OUTPUT_DIR / "output.json"
        with open(output_path, 'r+') as f:
            data = json.load(f)
            data["courses"].append(self.text)
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()

    def clean_up(self):
        """Remove all files in the output directory."""
        for file in INBETWEENS.glob('*'):
            file.unlink()




base = TextExtraction(r".\images\19.jpg")
base.write()
print(base.printable())
