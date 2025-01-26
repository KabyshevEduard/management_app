from pydantic import BaseModel, Field, model_validator
from datetime import datetime
from typing import Optional

#users 
class UserRegisterSchema(BaseModel):
    phone: str = Field(max_length=11, min_length=11)
    name: str
    password: str = Field(min_length=8, max_length=100)
    second_password: str = Field(min_length=8, max_length=100)

    @model_validator(mode='after')
    def check_password(self):
        if self.second_password != self.password:
            raise ValueError('Passwords are different')
        return self


class UserLoginSchema(BaseModel):
    phone: str = Field(max_length=11, min_length=11)
    password: str = Field(min_length=8, max_length=100)


class AddUserSchema(BaseModel):
    employe_id: int
    field_id: int


#fiels
class FieldSchema(BaseModel):
    id: int
    title: str
    discription: Optional[str]
    create_at: Optional[datetime]
    updated_at: Optional[datetime]


#message
class SendMessageSchema(BaseModel):
    content: str


class GetMessageSchema(BaseModel):
    created_at: datetime
    content: str

