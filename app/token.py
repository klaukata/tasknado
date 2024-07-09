from datetime import datetime, timezone, timedelta
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

o2auth_scheme = OAuth2PasswordBearer('/auth/login')

# these 3 should be env var in a real case scenario :)
SECRET_KEY ='SECRET'
ALGORITHM = 'HS256'
EXPIRY_MINUTES = 1000 # TODO - change this val back to 10

def create_token(sub_dict: dict) -> str:
    payload = sub_dict.copy()
    exp_time = datetime.now(timezone.utc) + timedelta(minutes=EXPIRY_MINUTES) # TODO - check if this time is not f up
    payload.update({'exp': exp_time})
    token = jwt.encode(payload, SECRET_KEY, ALGORITHM)
    return token

def decode_token(token: str):
    exception = HTTPException(
        status_code = 401,
        detail = 'your token is all wrong, my friend'
    )
    try:
        decoded = jwt.decode(token, SECRET_KEY, ALGORITHM)
        username = decoded.get('sub')
        return username
    except JWTError:
        raise exception