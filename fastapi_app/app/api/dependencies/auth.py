from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt import PyJWTError

from app.services.jwt import decode_token
from app.db.repositories.user import get_user_by_id
from app.model.schemas.user import UserInDb

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], user_by_id=Depends(get_user_by_id)) -> UserInDb:
    credentails_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decode_token(token)
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentails_exception
    except PyJWTError:
        raise credentails_exception
    user = await user_by_id(user_id=user_id)
    if user is None:
        raise credentails_exception
    return user
