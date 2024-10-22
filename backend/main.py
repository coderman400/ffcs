# main.py
import shutil

from fastapi import (BackgroundTasks, FastAPI, File, Form, UploadFile)
from fastapi.middleware.cors import CORSMiddleware
from tqdm import tqdm

from config import ROOT_DIR, UPLOADS
from core.utils.extraction import TextExtraction
from core.utils.pipeline import Pipeline
from core.utils.restructure import Restructure

app = FastAPI()

# Configure CORS to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://ffcs-frontend.onrender.com"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

def clean_up():
    for file in UPLOADS.iterdir():
        file.unlink()

def extract(image_paths):
    """Extract text from images"""
    data = {"courses" : []}
    for image_path in tqdm(image_paths):
        base = TextExtraction(image_path)
        data["courses"].append(base.text)
    
    return data


@app.post("/process/")
def upload_images(
    background_tasks: BackgroundTasks,
    image: list[UploadFile] = File(...),
    credits: str = Form(...),
    timing: str = Form(...)
):
    """API for generating timetables from uploaded images."""
    file_paths = []

    for file in image:
        file_location = UPLOADS / file.filename
        file_paths.append(str(file_location))

        with open(str(file_location), "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

    timing = True if timing == "morning" else False

    image_data = extract(file_paths)
    restructured_data = Restructure(image_data).data
    pipeline = Pipeline(restructured_data, morning=timing, credits=int(credits))
    
    background_tasks.add_task(clean_up)

    return pipeline.response


import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)