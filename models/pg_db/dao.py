from models.database import async_session_maker
from models.pg_db.models import User, Field, UserField, Message
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.future import select
from sqlalchemy import update as sqlalchemy_update, delete as sqlalchemy_delete, func


class BaseDAO:
    model = None

    @classmethod
    async def find_one_or_none_by_id(cls, data_id: int):
        async with async_session_maker() as session:
            q = select(cls.model).filter_by(id=data_id)
            result = await session.execute(q)
            return result.scalar_one_or_none()
        
    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            q = select(cls.model).filter_by(**filter_by)
            result = await session.execute(q)
            return result.scalar_one_or_none()
        
    @classmethod
    async def find_all_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            q = select(cls.model).filter_by(**filter_by)
            result = await session.execute(q)
            return result.scalars().all()
        
    @classmethod
    async def add(cls, **values):
        async with async_session_maker() as session:
            new_instance = cls.model(**values)
            session.add(new_instance)
            try:
                await session.commit()
            except SQLAlchemyError as e:
                await session.rollback()
                raise e
            return new_instance
              

class UserDAO(BaseDAO):
    model = User


class UserFieldDAO(BaseDAO):
    model = UserField

    @classmethod
    async def find_fields(cls, user_id):
        async with async_session_maker() as session:
            stmt = select(Field).where(cls.model.employe_id==user_id).join(cls.model)
            result = await session.execute(stmt)
            return result.scalars().all()

    @classmethod
    async def add(cls, **values):
        async with async_session_maker() as session:
            new_instance = cls.model(**values)
            session.add(new_instance)
            try:
                await session.commit()
            except SQLAlchemyError as e:
                await session.rollback()
                raise e

            return new_instance


class FieldDAO(BaseDAO):
    model = Field

    @classmethod
    async def add(cls, user_id, **values):
        async with async_session_maker() as session:
            new_instance_field = cls.model(**values)
            new_instance_user_field = UserField(employe_id=user_id, field=new_instance_field)
            session.add(new_instance_user_field)
            try:
                await session.commit()
            except SQLAlchemyError as e:
                await session.rollback()
                raise e
            return new_instance_field


class MessageDAO(BaseDAO):
    model = Message
    
