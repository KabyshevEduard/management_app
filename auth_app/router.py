from fastapi import APIRouter, HTTPException, status, Response, Request
from models.pg_db.auth import verify_password, get_password_hash, authenticate_user
from models.pg_db.dao import UserDAO, FieldDAO, UserFieldDAO, MessageDAO
from models.mongo.dao import DocumentDAO
from models.pg_db.schemas import UserRegisterSchema, UserLoginSchema
from models.pg_db.jwt import create_access_token

router = APIRouter(prefix='/auth', tags=['Auth'])


@router.post('/register')
async def register(item: UserRegisterSchema):
    user = await UserDAO.find_one_or_none(phone=item.phone)
    if user:
        return {'status': 'User already exist'}

    hashed_password = get_password_hash(item.password)
    try:
        await UserDAO.add(phone=item.phone, name=item.name, hashed_password=hashed_password)
        return {'status': 'success'}
    except Exception as e:
        return {'status': str(e)}
    

@router.post('/login')
async def login(request: Request, response: Response, item: UserLoginSchema):
    user = await authenticate_user(phone=item.phone, password=item.password)
    if user == None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Phone or password are incorrect')
    
    access_token = create_access_token({'sub': str(user.id)})
    response.set_cookie('user_access_token', access_token, httponly=True)
    return {'status': 'logged_in', 'user_access_token': access_token}




