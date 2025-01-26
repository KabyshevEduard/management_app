from sqlalchemy import String, Integer, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.database import Base
from typing import List, Optional

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement='auto')
    phone: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)

    user_field_user: Mapped['UserField'] = relationship(back_populates='employe')

    def __repr__(self):
        return f'User(id={self.id}, phone={self.phone}, name={self.name}, hashed_password={self.hashed_password})' 
    

class Field(Base):
    __tablename__ = 'fields'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement='auto')
    title: Mapped[str] = mapped_column(String(30))
    discription: Mapped[str] = mapped_column(Text, nullable=True)
    count_of_documents: Mapped[str] = mapped_column(Integer, default=0)
    count_of_employes: Mapped[str] = mapped_column(Integer, default=0)

    user_field_field: Mapped['UserField'] = relationship(back_populates='field')

    def __repr__(self):
        return f'Field(id={self.id}, title={self.title}, discription={self.discription}, count_of_documents={self.count_of_documents}, count_of_employes={self.count_of_employes})'
    

class UserField(Base):
    __tablename__ = 'user_field'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement='auto')
    employe_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    field_id: Mapped[int] = mapped_column(ForeignKey('fields.id'))

    employe: Mapped['User'] = relationship(back_populates='user_field_user')
    field: Mapped['Field'] = relationship(back_populates='user_field_field')

    def __repr__(self):
        return f'UserField(id={self.id}, employe_id={self.employe_id}, field_id={self.field_id})'
    

class Message(Base):
    __tablename__ = 'messages'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement='auto')
    from_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    to_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)


    def __repr__(self):
        return f'Message(id={self.id}, from_id={self.from_id}, to_id={self.to_id}, content={self.content})'
