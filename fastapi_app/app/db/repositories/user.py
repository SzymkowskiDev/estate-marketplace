from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.model.domain.user import User


async def get_user_by_username(async_session: AsyncSession, username: str):
    return await async_session.execute(select(User).where(User.username == username))


async def get_user_by_email(async_session: AsyncSession, email: str):
    return await async_session.execute(select(User).where(User.email == email))


async def get_user_by_id(async_session: AsyncSession, user_id: int):
    return await async_session.get(User).where(User.id == user_id).first()


async def create_user(async_session: AsyncSession, user: User):
    return await async_session.add(user)
