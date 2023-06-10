from sqlalchemy import Column, Integer, ForeignKey, Table
from app.db.base import Base

user_conversation = Table('association', Base.metadata,
                          Column('user_id', ForeignKey('users.id'), primary_key=True),
                          Column('conversation_id', ForeignKey('conversations.id'), primary_key=True)
                    )