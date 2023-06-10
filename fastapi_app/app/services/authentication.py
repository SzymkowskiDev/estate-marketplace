from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.user import get_user_by_email, get_user_by_username


class UsernameAlreadyTaken(Exception):
    def __init__(self, username: str):
        self.username = username
        super().__init__(f"User with username {self.username} already exists.")


class EmailAlreadyTaken(Exception):
    def __init__(self, email: str):
        self.email = email
        super().__init__(f"User with email {self.email} already exists.")


async def check_username_is_taken(async_session: AsyncSession, username: str) -> bool:
    found = await get_user_by_username(async_session=async_session, username=username)
    if found:
        raise UsernameAlreadyTaken(username=username)


async def check_email_is_taken(async_session: AsyncSession, email: str) -> bool:
    found = await get_user_by_email(async_session=async_session, email=email)
    if found:
        raise EmailAlreadyTaken(email=email)
