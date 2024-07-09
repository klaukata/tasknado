from datetime import datetime, timezone, timedelta
import jwt

# these 3 should be env var in a real case scenario :)
SECRET_KEY ='SECRET'
ALGORITHM = 'HS256'
EXPIRY_MINUTES = 10

def create_token(sub_dict: dict) -> dict:
    payload = sub_dict.copy()
    exp_time = datetime.now(timezone.utc) + timedelta(minutes=EXPIRY_MINUTES)
    payload.update({'exp': exp_time})
    token = jwt.encode(payload, SECRET_KEY, ALGORITHM)
    return {
        'token': token
    }