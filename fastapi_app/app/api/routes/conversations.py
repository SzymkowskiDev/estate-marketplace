from typing import List, Annotated

from fastapi import APIRouter, HTTPException, Depends, status, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.base import get_session

from app.model.schemas.user import UserInDb
from app.api.dependencies.auth import get_current_user

from app.model.domain.conversation import Conversation
from app.model.schemas.conversation import ConversationInCreate, ConversationInResponse
import app.db.repositories.conversation as conversations_repository
import app.db.repositories.message as messages_repository
from app.model.domain.message import Message
from app.model.schemas.message import MessageInCreate, MessageInResponse

from app.services.messages import notify_participants

router = APIRouter(
    prefix="/conversations",
    tags=["conversations"])


@router.get("/",
            response_model=List[ConversationInResponse])
async def get_all(user: Annotated[UserInDb, Depends(get_current_user)], session: AsyncSession = Depends(get_session)):
    return await conversations_repository.get_conversations_by_user_id(session, user.id)


@router.get("/{conversation_id}/",
            response_model=ConversationInResponse)
async def get_by_id(conversation_id: int,
                    user: Annotated[UserInDb, Depends(get_current_user)], session: AsyncSession = Depends(get_session)):
    conversation = await conversations_repository.get_conversation_by_id(session, conversation_id=conversation_id)
    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")

    if user not in conversation.participants:
        raise HTTPException(status_code=403, detail="User not in conversation")

    return conversation


@router.post("/", response_model=ConversationInResponse)
async def post_conversation(conversation_dto: ConversationInCreate,
                            user: Annotated[UserInDb, Depends(get_current_user)],
                            session: AsyncSession = Depends(get_session)):
    conversation = Conversation(**conversation_dto.dict())
    conversation.participants.push(user)
    return await conversations_repository.create_conversation(session, conversation)


@router.post("/{conversation_id}/messages")
async def post_message(conversation_id: int, message_dto: MessageInCreate,
                       user: Annotated[UserInDb, Depends(get_current_user)], background_tasks: BackgroundTasks,
                       session: AsyncSession = Depends(get_session)):
    conversation = await conversations_repository.get_conversation_by_id(session, conversation_id=conversation_id)
    if user not in conversation.participants:
        raise HTTPException(status_code=403, detail="User not in conversation")
    message = Message(**message_dto.dict())
    message.sender = user
    conversation.messages.append(message)

    await conversations_repository.update_conversation(conversation)

    background_tasks.add_task(notify_participants, conversation, message)
    return {"message": "Message sent"}


@router.get("/{conversation_id}/messages/", response_model=List[MessageInResponse])
async def get_messages(conversation_id: int, user: Annotated[UserInDb, Depends(get_current_user)],session: AsyncSession = Depends(get_session)):
    conversation = await conversations_repository.get_conversation_by_id(session, conversation_id=conversation_id)
    if user not in conversation.participants:
        raise HTTPException(status_code=403, detail="User not in conversation")
    return conversation.messages


@router.put("/{conversation_id}/messages/{message_id}/")
async def soft_delete_message(conversation_id: int, message_id: int,
                              user: Annotated[UserInDb, Depends(get_current_user)],session: AsyncSession = Depends(get_session)):
    conversation = await conversations_repository.get_conversation_by_id(session, conversation_id=conversation_id)
    if user not in conversation.participants:
        raise HTTPException(status_code=403, detail="User not in conversation")
    message = conversation.messages.filter_by(id=message_id).first()
    if not message:
        raise HTTPException(status_code=404, detail="Message not found")
    if message.sender != user:
        raise HTTPException(status_code=403, detail="User not message owner")
    await messages_repository.soft_delete_message(message_id=message_id)
