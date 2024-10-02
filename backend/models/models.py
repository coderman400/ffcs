# models.py
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True)
    title = Column(String)
    professors = relationship("Professor", back_populates="course")

class Professor(Base):
    __tablename__ = 'professors'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    course_id = Column(Integer, ForeignKey('courses.id'))
    course = relationship("Course", back_populates="professors")
    slots = relationship("Slot", back_populates="professor")

class Slot(Base):
    __tablename__ = 'slots'
    id = Column(Integer, primary_key=True, index=True)
    professor_id = Column(Integer, ForeignKey('professors.id'))
    professor = relationship("Professor", back_populates="slots")
    slot_info = Column(String)  # This will store the slot information like "C1,C2,L15+L16,L35+L36"
