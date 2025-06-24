from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
print("[DEBUG] Using URI:", MONGO_URI)

try:
    client = MongoClient(MONGO_URI)
    client.admin.command("ping")
    print("[✅ MongoDB] Connection successful!")
except Exception as e:
    print("[❌ MongoDB] Connection failed:", e)

db = client["VictimLink"]
collection = db["evidence_logs"]
