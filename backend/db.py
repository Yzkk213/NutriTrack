from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client["nutritrack"]

from pymongo import ReturnDocument

def get_next_meal_number() -> int:

    counter_doc = db["counters"].find_one_and_update(
        {"_id": "meal_counter"},
        {"$inc": {"value": 1}},
        upsert=True,
        return_document=ReturnDocument.AFTER
    )
    return counter_doc["value"]
