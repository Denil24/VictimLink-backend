# 📁 backend/app/utils/mongo.py

from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()  # ✅ Load environment variables from .env

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
collection = client["VictimLink"]["evidence"]  # Adjust DB & collection names if needed

try:
    client.admin.command("ping")
    print("[✅ MongoDB] Connected successfully.")
except Exception as e:
    print(f"[❌ MongoDB] Connection failed: {e}")
