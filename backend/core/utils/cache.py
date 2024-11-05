import uuid
import json
from config import ROOT_DIR

class Cache:
    def __init__(self,data):
        self.data = data
        self.id = self.cache_it(data)

    def cache_it(self,data):
        id = str(uuid.uuid4())
        with open(ROOT_DIR / "cache" / f"{id}.json", "w") as file: 
            json.dump(data, file)
        return id

    def retrieve(id):
        with open(ROOT_DIR / "cache" / f"{id}.json", "r") as file:
            data = json.load(file)
        Cache.delete_it(id)
        return data
    
    def delete_it(id):
        (ROOT_DIR / "cache" / f"{id}.json").unlink()