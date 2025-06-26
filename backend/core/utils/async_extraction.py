import asyncio
import json
import os
import textwrap
from pathlib import Path

import google.generativeai as genai
import numpy as np
from dotenv import load_dotenv

from config import ROOT_DIR


class TextExtraction:
    def __init__(self, image_path: str):
        self.image_path = Path(image_path)
        self.setup_genai()
        self.text = None
        self.reformat = None
         # Initialize the extraction process asynchronously

    def setup_genai(self):
        """Setup GenAI with API key and configuration."""
        load_dotenv()
        genai.configure(api_key=os.getenv("api_key"))
        self.genai_image = genai.upload_file(str(self.image_path))
        self.model = genai.GenerativeModel("gemini-2.0-flash", tools=self.tools())

    async def _init_extraction(self):
        """Initialize the text extraction process asynchronously."""
        self.text = await self.extract()  # Extract text asynchronously
        await self.post_process()  # Post-process the extracted data asynchronously
        self.reformat = await self.reformatter()  # Reformat asynchronously

    async def extract(self):
        """Extract text from the image using GenAI asynchronously."""
        result = await asyncio.to_thread(self.model.generate_content, [   
            self.genai_image,
            "Extract slot detail, faculty, course type from the image. Extract the course code and title information as well. ",],
            tool_config={'function_calling_config': 'ANY'}
        )
        fc = result.candidates[0].content.parts[0].function_call
        data = type(fc).to_dict(fc)
        return data["args"]
    
    def tools(self):
        """Define the tools schema for GenAI."""
        slot = genai.protos.Schema(
            type=genai.protos.Type.OBJECT,
            properties={
                'faculty': genai.protos.Schema(type=genai.protos.Type.STRING),
                'slot': genai.protos.Schema(type=genai.protos.Type.STRING),
                'course_type': genai.protos.Schema(type=genai.protos.Type.STRING),
            },
            required=['faculty', 'slot', 'course_type']
        )

        slots = genai.protos.Schema(
            type=genai.protos.Type.ARRAY,
            items=slot
        )

        extract = genai.protos.FunctionDeclaration(
            name="add_to_database",
            description=textwrap.dedent("""\
                Adds entities to the database.
                """),
            parameters=genai.protos.Schema(
                type=genai.protos.Type.OBJECT,
                properties={
                    'course_code': genai.protos.Schema(type=genai.protos.Type.STRING),
                    'course_title': genai.protos.Schema(type=genai.protos.Type.STRING),
                    'slots': slots
                }
            )
        )

        return [extract]

    async def post_process(self):
        """Post-process the extracted text asynchronously."""
        data = self.text
        for slot in data['slots']:
            slot['prof'] = slot.pop('faculty')
            slot['slots'] = slot.pop('slot')
        
        code = data['course_code']
        title = data['course_title']
        data['title'] = title.strip()
        data['code'] = code.strip()

        del data['course_code']
        del data['course_title']

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

    async def reformatter(self):
        """Reformat the extracted text asynchronously."""
        reformat = {"code": self.text["code"], "title": self.text["title"], "slots": []}
        reformat["slots"] = [*set([slot["slots"] for slot in self.text["slots"]])]
        return reformat
