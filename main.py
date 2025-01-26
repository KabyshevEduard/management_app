from fastapi import FastAPI
from auth_app.router import router as auth_router
from field_app.router import router as field_router
from document_app.router import router as document_router
from message_app.router import router as message_router

app = FastAPI()
@app.get('/')
async def home_page():
    return {'Main page': 'success'}


app.include_router(auth_router)
app.include_router(field_router)
app.include_router(document_router)
app.include_router(message_router)