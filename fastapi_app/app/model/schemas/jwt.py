from datetime import datetime

from pydantic import BaseModel


class JWTMeta(BaseModel):
    exp: datetime
    sub: str

class JWTUser(BaseModel):
    id: str
    username: str
    email: str

    class Config:
        orm_mode = True
