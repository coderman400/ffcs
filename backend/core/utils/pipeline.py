import json
import os

from fastapi import Depends
from sqlalchemy.orm import Session
from tqdm import tqdm

from models.crud import create_course
from models.database import get_db

from ..ffcs.algorithm import Algorithm
from .extraction import TextExtraction
from .restructure import Restructure


class Pipeline:
    def __init__(self,image_paths,db):
        self.image_paths = image_paths
        self.db = db
        self.json_path = self.extract()
        self.add_to_db()
        self.restructured = Restructure(self.json_path)
        self.base = Algorithm(self.restructured.data)
        self.response = self.make_response(self.base.results)
        

    def add_to_db(self):
        with open(self.json_path) as f:
            data = json.load(f)
        for course in data["courses"]:
            print(course["code"])
            create_course(self.db,course)

        
    def extract(self):
        """Extract text from images."""
        for image_path in tqdm(self.image_paths):
            base = TextExtraction(image_path)
            path = base.write()

        return path
    
    
    def make_response(self,data):
        final = {"slots" : []}
        flatten = lambda data : [(x,"+".join(y).split("+")) for x,y in data]

        for timetable in data:
            data = flatten(timetable)
            response = {slot:course for course,slots in data for slot in slots}
            final["slots"].append(response)

        return final