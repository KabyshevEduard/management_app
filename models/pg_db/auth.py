from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta, timezone
from models.pg_db.dao import UserDAO

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def get_password_hash(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


async def authenticate_user(phone, password):
    user = await UserDAO.find_one_or_none(phone=phone)
    if not user or not verify_password(password, user.hashed_password):
        return None
    
    return user
