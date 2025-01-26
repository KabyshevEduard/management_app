from models.pg_db.dao import UserDAO, FieldDAO, UserFieldDAO
from models.mongo.dao import DocumentDAO
from models.pg_db.schemas import FieldSchema, AddUserSchema
from models.pg_db.jwt import check_token
from fastapi import APIRouter, Request, Response, HTTPException, status
from typing import List

router = APIRouter(prefix='/field', tags=['Filed'])


@router.post('/add_field')
async def add_field_view(request: Request, item: FieldSchema):
    token = request.cookies.get('user_access_token')
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Not logged in')
    
    user_id = check_token(token)
    await FieldDAO.add(user_id, title=item.title, discription=item.discription)
    return {'status': 'success', 'Attention': 'Create chat in telegram with same title and NotifyDocumentManager in it. Dont forget make him an administrator'}


@router.get('/all', response_model=List[FieldSchema])
async def all_fields_view(request: Request):
    token = request.cookies.get('user_access_token')
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Not logged in')
    
    user_id = check_token(token)
    fields = await UserFieldDAO.find_fields(user_id)
    return fields


@router.get('/add_employe')
async def add_employe_view(request: Request, item: AddUserSchema):
    token = request.cookies.get('user_access_token')
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Not logged in')
    
    check_token(token)
    await UserFieldDAO.add(employe_id=item.employe_id, field_id=item.field_id)
    return {'status': 'success'}
