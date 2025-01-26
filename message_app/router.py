from models.pg_db.dao import MessageDAO
from models.pg_db.schemas import SendMessageSchema
from models.pg_db.jwt import check_token
from models.database import database_url_redis
from models.redis.dao import PubSubDAO 
from fastapi import APIRouter, Request, Response, HTTPException, status, WebSocket, WebSocketDisconnect
from typing import List, Any
from datetime import datetime


router = APIRouter(prefix='/message', tags=['Message'])

@router.post('/{user_id_to}')
async def send_message(user_id_to: int, request: Request, item: SendMessageSchema):
    token = request.cookies.get('user_access_token')
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Not logged in')
    
    user_id = check_token(token)
    await MessageDAO.add(from_id=user_id, to_id=user_id_to, content=item.content)
    name1 = str(user_id) + str(user_id_to)
    name2 = str(user_id_to) + str(user_id)
    await PubSubDAO.send_in_pub(name1, item.content)
    await PubSubDAO.send_in_pub(name2, item.content)
    return {'status': 'success'}


@router.websocket('/ws/{user_access_token}/{user_id_to}')
async def websocket_endpoint(websocket: WebSocket, user_access_token: str, user_id_to: int):    
    user_id = check_token(user_access_token)
    name = str(user_id) + str(user_id_to)
    await websocket.accept()
    try:
        async for mes in PubSubDAO.subscribe_getting_pub(name):
                await websocket.send_text(mes)
                continue
                #await websocket.send_text(data)

    except WebSocketDisconnect:
        await PubSubDAO.send_in_pub(name, PubSubDAO.stopword)
