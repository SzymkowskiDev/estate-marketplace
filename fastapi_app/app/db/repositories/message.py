from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.model.domain.message import Message


def get_message_by_id(async_session: AsyncSession, message_id: int) -> Optional[Message]:
    return async_session.query(Message).filter(Message.id == message_id).first()


def create_message(async_session: AsyncSession, message: Message) -> Message:
    async_session.add(message)
    async_session.commit()
    async_session.refresh(message)
    return message


def soft_delete_message(async_session: AsyncSession, message_id: int) -> Message:
    message = async_session.query(Message).filter(Message.id == message_id).first()
    message.deleted = True
    async_session.commit()
    async_session.refresh(message)
    return message


def delete_message(async_session: AsyncSession, message_id: int) -> Message:
    message = async_session.query(Message).filter(Message.id == message_id).first()
    async_session.delete(message)
    async_session.commit()
    return message
