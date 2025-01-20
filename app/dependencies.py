from pymongo import MongoClient
from app.adapters.db_adapter import MongoDBAdapter
from app.config import Config
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient(Config.MONGODB_URL)
db = client.store
collection = db.get_collection("products")
db_adapter = MongoDBAdapter(collection)

def get_db_adapter():
    return db_adapter
