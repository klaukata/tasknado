from fastapi import APIRouter, Depends
from ..auth import o2auth_scheme, decode_token
from ..crud import get_user, display_user_details

router = APIRouter()

@router.get('/me')
def read_logged_user(token: str = Depends(o2auth_scheme)):
    decoded_username = decode_token(token)
    user_doc = get_user(decoded_username)
    return display_user_details(user_doc)