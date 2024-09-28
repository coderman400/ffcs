# main.py
import shutil

from fastapi import (BackgroundTasks, Depends, FastAPI, File, HTTPException,
                     UploadFile, WebSocket, WebSocketDisconnect)
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from config import ROOT_DIR, UPLOADS
from core.utils.pipeline import Pipeline
from models import crud, models, schemas
from models.database import engine, get_db

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


async def timetable_generation(websocket: WebSocket,file_paths,db):
    pipeline = await Pipeline(file_paths,db)
    print(pipeline.response)
    return pipeline.response


@app.post("/process/")
def upload_images(background_tasks:BackgroundTasks,image: list[UploadFile] = File(...),db: Session = Depends(get_db)):
    file_paths = []

    for file in image:
        file_location = UPLOADS / file.filename
        file_paths.append(str(file_location))

        with open(str(file_location), "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

    pipeline = Pipeline(file_paths,db)
    print(pipeline.response)

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