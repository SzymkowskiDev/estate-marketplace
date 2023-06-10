from typing import List, Optional

from pydantic import BaseModel, Field

from app.model.schemas.message import MessageInResponse
from app.model.schemas.user import UserInResponse

DEFAULT_CONVERSATIONS_LIMIT = 20
DEFAULT_CONVERSATIONS_OFFSET = 0

class ConversationInCreate(BaseModel):
    participants: List[int]

    class Config:
        orm_mode = True

class ConversationInResponse(BaseModel):
    id: int
    participants: List[UserInResponse]
    messages: List[MessageInResponse]

    class Config:
        orm_mode = True

class ConversationsFilters(BaseModel):
    limit: int = Field(DEFAULT_CONVERSATIONS_LIMIT, ge=1)
    offset: int = Field(DEFAULT_CONVERSATIONS_OFFSET, ge=0)

    class Config:
        orm_mode = True

class ListOfConversationsInResponse(BaseModel):
    conversations: List[ConversationInResponse]
    total: int
    limit: int
    offset: int
    has_next: bool
    has_previous: bool
    next_offset: int | None = None
    previous_offset: int | None = None

    class Config:
        orm_mode = True

