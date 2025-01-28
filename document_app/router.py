from models.mongo.dao import DocumentDAO, TgIdsDAO
from models.pg_db.dao import FieldDAO, UserDAO
from models.pg_db.jwt import check_token
from models.database import database_url_redis
from fastapi import APIRouter, Request, Response, HTTPException, status, UploadFile
from typing import List, Any
from datetime import datetime
import ast
import pydantic
from bson import ObjectId
from ML_app.schemas import MLSchema

from celery_app.celery import save_file, send_notification

import grpc
import ML_app.protobuf_pb2_grpc as protobuf_pb2_grpc
from ML_app.protobuf_pb2 import MessageRequest, PredictResponse



router = APIRouter(prefix='/document', tags=['Document'])


@router.post('/add')
async def add_document_view(request: Request, item: str, file: UploadFile):
    token = request.cookies.get('user_access_token')
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Not logged in')
    
    user_id = check_token(token)
    data = ast.literal_eval(item)
    if ('field_id' not in data):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Key field_id is not found')
    
    #add document
    path = '/home/e2rd/Desktop/management_app/models/mongo/pdfs/' + str(user_id) + '_' + str(data['field_id']) + '_' + file.filename
    date_now = datetime.now()
    data['date_added'] = date_now
    data['file_path'] = path
    data['owner_id'] = user_id
    data['field_id'] = int(data['field_id'])
    await DocumentDAO.add(data)

    #celery save file
    bin_content = await file.read()
    result = save_file
    saving = result.delay(bin_content, path)
    saving.get()

    #add tg chat
    q = await FieldDAO.find_one_or_none_by_id(data['field_id'])
    chat_title = q.title
    user = await UserDAO.find_one_or_none_by_id(user_id)
    name = user.name

    #celery notify
    notify = send_notification
    notify.delay(name, chat_title)
    
    return {'status': 'success'}


@router.post('/ml')
async def send_ml(request: Request, item: MLSchema):
    token = request.cookies.get('user_access_token')
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Not logged in')
    
    user_id = check_token(token)
    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        stub = protobuf_pb2_grpc.PredictionServiceStub(channel)
        request = MessageRequest(token=token, message_id=item.message_id, text=item.text, type_id=item.type_id, rating=item.rating)
        response = await stub.MakePred(request)
        print(response)
    return {'status': 'success'}
