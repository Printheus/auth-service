from fastapi import Depends, Response, exceptions, status
from fastapi.routing import APIRouter
from auth_service.core.database import get_db
from auth_service.core.utils import create_access_token
from .schema import LoginRequestData
from .engine import BasicAuthEngine

# add views heres

router = APIRouter()


@router.post("/login", name="basic_login")
async def log_in(data: LoginRequestData, response: Response, db=Depends(get_db)):
    user = await BasicAuthEngine(db).authenticate(data)
    if user is None:
        raise exceptions.HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    role = "admin" if user.is_admin else "base"
    token = create_access_token(
        subject=str(user.user_id), username=user.username, user_role=role
    )

    response.set_cookie(
        key="Access-Token",
        value=token,
        secure=True,
        httponly=True,
        samesite="strict",
    )
    return None
