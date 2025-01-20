import os

class Config:
    MONGODB_URL = os.getenv("MONGODB_URL")
