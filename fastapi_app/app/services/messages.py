from app.model.domain.message import Message
from app.model.domain.conversation import Conversation
from loguru import logger


async def notify_participants(conversation: Conversation, message: Message):
    logger.info(f"Sending notification to participants of conversation {conversation.id}")