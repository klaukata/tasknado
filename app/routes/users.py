from fastapi import APIRouter, Depends
from ..token import o2auth_scheme, decode_token
router = APIRouter()

@router.get('/me')
def read_logged_user(token: str = Depends(o2auth_scheme)):
    decoded = decode_token(token)
    return decoded