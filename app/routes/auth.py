from fastapi import APIRouter, HTTPException
from ..database import users_collection
from ..crud import create_user
from ..models import User

router = APIRouter()

@router.post('/register')
def register(user_details: User):
    username = user_details.username
    user_doc = users_collection.find_one({'username': username})
    if user_doc == None:
        return create_user(user_details)
    return HTTPException(
        status_code=404,
        detail='Username is taken, dude :/',
        headers={'WWW-Authenticate': 'Bearer'}
    )

@router.post('/login')
def login_for_token():
    pass