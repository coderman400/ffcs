# main.py
import shutil

from fastapi import (BackgroundTasks, Depends, FastAPI, File, HTTPException,
                     UploadFile,Form)
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from config import ROOT_DIR, UPLOADS
from core.utils.pipeline import Pipeline
from core.utils.extraction import TextExtraction
from core.utils.restructure import Restructure
from models import crud, models, schemas
from models.database import engine, get_db

from tqdm import tqdm
models.Base.metadata.create_all(bind=engine)


app = FastAPI()

# Configure CORS to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

def clean_up():
    for file in UPLOADS.iterdir():
        file.unlink()

def extract(image_paths):
    """Extract text from images."""
    data = {"courses" : []}
    for image_path in tqdm(image_paths):
        base = TextExtraction(image_path)
        base.write()
        data["courses"].append(base.text)
    
    print(f"Done extracting --> {len(data["courses"])} courses.")
    return data


@app.post("/process/")
def upload_images(
    background_tasks: BackgroundTasks,
    image: list[UploadFile] = File(...),
    credits: str = Form(...),
    timing: str = Form(...),
    db: Session = Depends(get_db)
):
    file_paths = []

    for file in image:
        file_location = UPLOADS / file.filename
        file_paths.append(str(file_location))

        with open(str(file_location), "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

    # You can now access credits and timing here
    print(f"Credits: {credits}, Timing: {timing}")
    timing = True if timing == "morning" else False

    image_data = extract(file_paths)
    restructured_data = Restructure(image_data).data
    pipeline = Pipeline(restructured_data, morning=timing, creditsRequired=int(credits))
    
    background_tasks.add_task(clean_up)

    return pipeline.response



@app.get("/empty_db/")
def empty_database(db: Session = Depends(get_db)):
    try:
        # Delete all records from each table
        db.query(models.Slot).delete()
        db.query(models.Professor).delete()
        db.query(models.Course).delete()
        db.commit()  # Commit the changes
        return {"detail": "Database has been emptied successfully."}
    except Exception as e:
        db.rollback()  # Rollback in case of error
        raise HTTPException(status_code=500, detail=str(e))
    

import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)