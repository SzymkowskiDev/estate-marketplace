from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.model.domain.conversation import Conversation


def get_conversation_by_id(async_session: AsyncSession, conversation_id: int) -> Optional[Conversation]:
    return async_session.query(Conversation).filter(Conversation.id == conversation_id).first()


def create_conversation(async_session: AsyncSession, conversation: Conversation) -> Conversation:
    async_session.add(conversation)
    async_session.commit()
    async_session.refresh(conversation)
    return conversation


def get_conversations(async_session: AsyncSession) -> List[Conversation]:
    return async_session.query(Conversation).all()


def get_conversations_by_user_id(async_session: AsyncSession, user_id: int) -> List[Conversation]:
    return async_session.query(Conversation).filter(Conversation.user_id == user_id).all()


def update_conversation(async_session: AsyncSession, conversation: Conversation) -> Conversation:
    async_session.add(conversation)
    async_session.commit()
    async_session.refresh(conversation)
    return conversation
