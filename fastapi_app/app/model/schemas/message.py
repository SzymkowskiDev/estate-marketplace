from datetime import datetime
from pydantic import BaseModel
from .user import UserInResponse


class MessageInCreate(BaseModel):
    body: str


class MessageInResponse(BaseModel):
    id: int
    body: str
    sender: UserInResponse
    seen: bool
    seen_at: datetime | None = None
    created_at: datetime
    updated_at: datetime | None = None

class ListOfMessagesInResponse(BaseModel):
    messages: list[MessageInResponse]
    total: int
    limit: int
    offset: int
    has_next: bool
    has_previous: bool
    next_offset: int | None = None
    previous_offset: int | None = None