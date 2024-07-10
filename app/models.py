from pydantic import BaseModel
from bson import ObjectId

# auth router related models
class User(BaseModel):
    username: str
    email: str
    password: str

class Task(BaseModel):
    title: str
    description: str
    priority: int
    completed: bool
    owner: str