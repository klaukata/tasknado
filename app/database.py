from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.environ['MONGO_URI']
client = MongoClient(uri)

db = client.tasknado
users_collection = db.users
tasks_collection = db.tasks