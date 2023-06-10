from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.base import get_session
import app.services.register as register_service

from loguru import logger

from app.model.schemas.user import UserInCreate, UserInLogin

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register")
async def register(register_dto: UserInCreate, session: AsyncSession = Depends(get_session)):
    logger.info(f"register_dto: {register_dto}")
    return await register_service.register(session, register_dto)


@router.post("/login")
async def login(login_dto: UserInLogin, session: AsyncSession = Depends(get_session)):
    return await register_service.login(session, login_dto)
