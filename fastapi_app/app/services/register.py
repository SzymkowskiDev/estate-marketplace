import asyncio
from loguru import logger

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from app.model.domain.user import User
from app.model.schemas.user import UserInCreate, UserInLogin, UserInResponse, UserTokenResponse
from app.services.authentication import check_username_is_taken, check_email_is_taken, UsernameAlreadyTaken, \
    EmailAlreadyTaken
from app.services.jwt import create_access_token_for_user


async def register(async_session: AsyncSession, register_dto: UserInCreate):
    try:
        await asyncio.gather(
            check_username_is_taken(async_session=async_session, username=register_dto.username),
            check_email_is_taken(async_session=async_session, email=register_dto.email))
    except UsernameAlreadyTaken as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
    except EmailAlreadyTaken as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))

    logger.info(f"got here")
    user = User(**register_dto.dict())

    return UserInResponse.from_orm(user)


def login(db: AsyncSession, login_dto: UserInLogin):
    with db.begin() as async_session:
        user = async_session.get(User, email=login_dto.email)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    if not user.check_password(login_dto.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")
    at = create_access_token_for_user(user)
    return UserTokenResponse(access_token=at)
