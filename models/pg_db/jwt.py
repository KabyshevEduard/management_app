from jose import jwt, JWTError 
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException, status

SECRET_KEY = 'qpwoieurjhdjkhkdhfksjdhjk09d8fajhdyf876sd6f78dsfjhdskjhfkdsjhfi5s64f3s23f21fysdfdslfjsdl'
ALGORITHM = 'HS256'


def create_access_token(data: dict):
    data_to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=30)
    data_to_encode.update({'exp': expire})
    encode_jwt = jwt.encode(data_to_encode, SECRET_KEY, ALGORITHM)
    return encode_jwt


def check_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Wrong token or time is gone')
    
    user_id = payload.get('sub')
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Sub user id is not found')
    
    return int(user_id)
