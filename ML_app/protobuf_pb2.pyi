from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MessageRequest(_message.Message):
    __slots__ = ("token", "message_id", "text", "type_id", "rating")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    token: str
    message_id: int
    text: str
    type_id: int
    rating: float
    def __init__(self, token: _Optional[str] = ..., message_id: _Optional[int] = ..., text: _Optional[str] = ..., type_id: _Optional[int] = ..., rating: _Optional[float] = ...) -> None: ...

class PredictResponse(_message.Message):
    __slots__ = ("p",)
    P_FIELD_NUMBER: _ClassVar[int]
    p: float
    def __init__(self, p: _Optional[float] = ...) -> None: ...
