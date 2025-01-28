from pydantic import BaseModel, Field, model_validator
from datetime import datetime
from typing import Optional

#users 
class MLSchema(BaseModel):
    message_id: int
    text: str 
    type_id: int
    rating: float
