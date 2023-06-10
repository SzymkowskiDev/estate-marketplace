from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.orm import relationship

from app.db.timestamped import TimestampedBase

from .user_conversation import user_conversation


class Conversation(TimestampedBase):
    __tablename__ = "conversations"
    id = Column(Integer, primary_key=True)
    participants = relationship('User', secondary=user_conversation, back_populates='conversations')
    messages = relationship("Message", back_populates="conversation")