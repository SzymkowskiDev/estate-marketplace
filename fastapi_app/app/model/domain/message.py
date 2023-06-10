from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship

from app.db.timestamped import TimestampedBase

class Message(TimestampedBase):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(Integer, ForeignKey('conversations.id'))
    conversation = relationship("Conversation", back_populates="messages")
    body = Column(String)
    sender = Column(Integer, ForeignKey("users.id"))
    seen = Column(Boolean, default=False)
    seen_at = Column(DateTime, default=None)
    deleted = Column(Boolean, default=False)
    deleted_at = Column(DateTime, default=None)