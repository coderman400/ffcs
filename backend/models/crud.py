# crud.py
from sqlalchemy.orm import Session

from models import models, schemas


def create_course(db: Session, course_data: dict):
    # Check if the course already exists
    existing_course = db.query(models.Course).filter(models.Course.code == course_data['code']).first()
    if existing_course:
        # Course already exists, return None or handle accordingly
        return None

    # Create new course if it doesn't exist
    db_course = models.Course(
        code=course_data["code"],
        title=course_data["title"],
    )

    for slot in course_data["slots"]:
        db_professor = models.Professor(name=slot["prof"], course=db_course)
        db_course.professors.append(db_professor)

        # Create Slot instances
        db_slot = models.Slot(professor=db_professor, slot_info=slot["slots"])
        db_professor.slots.append(db_slot)

    db.add(db_course)
    db.commit()
    db.refresh(db_course)

    return db_course

