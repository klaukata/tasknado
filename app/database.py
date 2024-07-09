from pymongo import MongoClient
from dotenv import load_dotenv
import os

# load all env vars
load_dotenv() 

# get MONGO_URI env
uri = os.environ['MONGO_URI']

# mongo client & collections
client = MongoClient(uri)

db = client.tasknado
users_collection = db.users
tasks_collection = db.tasks