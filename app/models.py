from pydantic import BaseModel

# auth router related models
class User(BaseModel):
    username: str
    email: str
    password: str