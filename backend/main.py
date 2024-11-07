import asyncio
import json
from pathlib import Path

import aiofiles
from fastapi import (BackgroundTasks, Cookie, FastAPI, File, Form, Response,
                     UploadFile)
from fastapi.middleware.cors import CORSMiddleware

from config import ROOT_DIR, UPLOADS
from core.ffcs.algorithm import CourseScheduler as Algorithm
from core.utils.async_extraction import TextExtraction
from core.utils.cache import Cache
from core.utils.response import Response
from core.utils.restructure import Restructure

app = FastAPI()

# Configure CORS to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=".*",  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

def clean_up(file_paths: list):
    """Delete only the files specified in the file_paths list."""
    for file_path in file_paths:
        file = Path(file_path)
        if file.exists() and file.is_file():
            file.unlink()




async def extract(image_paths):
    """Extract text from images asynchronously."""
    reformat_data = []
    base_text = []

    # Run text extraction concurrently for each image
    tasks = []
    for image_path in image_paths:
        tasks.append(asyncio.create_task(process_image(image_path, reformat_data, base_text)))

    await asyncio.gather(*tasks)

    return {"base_reformat": reformat_data, "base_text": base_text}

async def process_image(image_path, reformat_data, base_text):
    """Process an image asynchronously."""
    base = TextExtraction(image_path)  # Assuming TextExtraction is a blocking operation
    await base._init_extraction()
    reformat_data.append(base.reformat)
    base_text.append(base.text)


@app.post("/process2/")
async def process_images(
    background_tasks: BackgroundTasks,
    image: list[UploadFile] = File(...),
):
    """API for generating timetables from uploaded images."""
    file_paths = []

    # Save files asynchronously
    for file in image:
        file_location = UPLOADS / file.filename
        file_paths.append(str(file_location))

        # Using aiofiles to handle file saving asynchronously
        async with aiofiles.open(str(file_location), 'wb') as buffer:
            await buffer.write(file.file.read())
    print(file_paths)
    # Call the async extract function
    image_data = await extract(file_paths)

    # Process the image_data as usual
    cache = Cache(image_data["base_text"])

    # Clean up in the background after processing
    background_tasks.add_task(lambda :clean_up(file_paths))
    print(image_data["base_reformat"],cache.id)

    return {"courses": image_data["base_reformat"], "id": cache.id}


@app.post("/process3/")
def process(
    session_token :str = Cookie(None),
    credits: str = Form(...),
    timing: str = Form(...),
    courses: str = Form(...),
    id: str = Form(...),
):
    print(id)
    courses = json.loads(courses)

    base_text = Cache.retrieve(id)

    restructured = Restructure({"courses": base_text})
    restructured.mandate(courses)
    restructured_data = restructured.data

    morning= True if timing == "morning" else False
    base = Algorithm(morning=morning, credits_required=int(credits), data=restructured_data)
    timetables = base.generate_schedules()
    
    response = Response(timetables,base_text).response
    return response


import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
