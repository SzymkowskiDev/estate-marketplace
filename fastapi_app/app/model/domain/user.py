from sqlalchemy import Column, Integer, String, event
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property

from app.db.timestamped import TimestampedBase
from app.services import security
from .user_conversation import user_conversation


class User(TimestampedBase):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    _password = Column('password', String)
    conversations = relationship('Conversation', secondary=user_conversation, back_populates='participants')

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = security.get_password_hash(password)

    def verify_password(self, password):
        return security.verify_password(password, self._password)


@event.listens_for(User, 'before_insert')
@event.listens_for(User, 'before_update')
def hash_password(mapper, connection, target):
    if target._password:
        target.password = target._password
