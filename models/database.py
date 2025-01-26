from sqlalchemy import func
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine, AsyncSession
from pymongo import AsyncMongoClient
import redis.asyncio as redis

database_url_pg = 'postgresql+asyncpg://e2rd:lex2mubds@172.18.0.2:5432/Document_orginizer'
engine = create_async_engine(url=database_url_pg)
async_session_maker = async_sessionmaker(engine, class_=AsyncSession)

database_url_mongo = 'mongodb://e2rd:lex2mubds@172.18.0.3:27017/'
async_client = AsyncMongoClient(database_url_mongo)
db = 'management'
collection_name = 'document'
collection = async_client[db][collection_name]
collection_tg = async_client[db]['tg_ids']

database_url_redis = 'redis://172.18.0.4'


class Base(AsyncAttrs, DeclarativeBase):
    create_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())
