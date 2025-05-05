from fastapi import Depends, Response, exceptions, status
from fastapi.routing import APIRouter
from logging import getLogger
from bcrypt import checkpw
from datetime import datetime, timedelta, timezone

from app.controllers import UserController
from app.database import get_db
from app.models import User
from app.schemas import LoginRequestData, UserCreate
from app.utils import create_token, bcrypt_hasher
from app.settings import settings

router = APIRouter()
logger = getLogger(__name__)


@router.post("/login", name="basic_login")
async def log_in(data: LoginRequestData, response: Response, db=Depends(get_db)):
    user = UserController(db).retrieve_by_username(data.username)
    if (user is None) or (not checkpw(data.password.encode(), user.password.encode())):
        logger.warning(f"Failed login attempt for username: {data.username}")
        raise exceptions.HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not user.is_active:
        logger.warning(f"Failed login attempt for deactivated user: {data.username}")
        raise exceptions.HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="user is not active"
        )

    role = "admin" if user.is_superuser else "base"

    access_token = create_token(
        payload={
            "sub": "Access-Token",
            "name": user.username,
            "id": str(user.user_id),
            "role": role,
        }
    )

    refresh_token = create_token(
        payload={"sub": "Refresh-Token"},
        expires_delta=timedelta(minutes=settings.REFRESH_TOKEN_EXPIRE),
    )

    response.set_cookie(
        key="Access-Token",
        value=access_token,
        secure=True,
        httponly=True,
        samesite="lax",
    )

    response.set_cookie(
        key="Refresh-Token",
        value=refresh_token,
        secure=True,
        httponly=True,
        samesite="strict",
    )

    return {"message": "Login successfully", "role": role, "Access_Token": access_token}


@router.post("/sign_up")
def signup(
    data: UserCreate,
    response: Response,
    db= Depends(get_db),
    ):
    data.password = bcrypt_hasher(data.password)
    user = User(**data.__dict__, date_joined=datetime.now(timezone.utc))
    db.add(user)
    try:
        db.commit()
        db.refresh(user)
    except Exception as e:
        raise Exception from e
    
    access_token = create_token(
        payload={
            "sub": "Access-Token",
            "name": user.username,
            "id": str(user.user_id),
            "role": "base",
        }
    )

    refresh_token = create_token(
        payload={"sub": "Refresh-Token"},
        expires_delta=timedelta(minutes=settings.REFRESH_TOKEN_EXPIRE),
    )

    response.set_cookie(
        key="Access-Token",
        value=access_token,
        secure=True,
        httponly=True,
        samesite="lax",
    )

    response.set_cookie(
        key="Refresh-Token",
        value=refresh_token,
        secure=True,
        httponly=True,
        samesite="strict",
    )

    return {"message": "Login successfully", "role": "base", "Access_Token": access_token}

