from pydantic import BaseModel, Field, model_validator, ConfigDict, Json
from datetime import datetime
from typing import Optional


class AddDocumentSchema(BaseModel):
    title: str = Field(max_length=30)
    discription: Optional[str]
    