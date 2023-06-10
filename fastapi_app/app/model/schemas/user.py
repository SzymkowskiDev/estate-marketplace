from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserInCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

    class Config:
        orm_mode = True


class UserInLogin(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True


class UserInResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True


class UserTokenResponse(BaseModel):
    access_token: str

    class Config:
        orm_mode = True


class UserInDb(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        orm_mode = True
