# schemas.py
from typing import List

from pydantic import BaseModel


class SlotCreate(BaseModel):
    prof: str
    slots: str  # This will be a comma-separated string of slots

class CourseCreate(BaseModel):
    code: str
    title: str
    slots: List[SlotCreate]  # Now this holds the slots information
