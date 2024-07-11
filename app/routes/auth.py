from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from ..database import users_collection
from ..crud import create_user, get_user
from ..models import User
from ..auth import create_token

router = APIRouter()

@router.post('/login')
def login_for_token(form: OAuth2PasswordRequestForm = Depends()) -> dict:
    user_doc = get_user(form.username)
    if user_doc == None or form.password != user_doc.password: # if username does not exist in a database or passwords do not match:
        raise HTTPException( # raise an error
            status_code=400,
            detail='Entered wrong password and/or username'
        )
    token = create_token({'sub': user_doc.username})
    return {
        'access_token': token,
        'token_type': 'bearer'
    }

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