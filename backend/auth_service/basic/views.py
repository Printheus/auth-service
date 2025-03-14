from logging import getLogger
from fastapi import Depends, Response, exceptions, status
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from auth_service.core.database import get_db
from auth_service.core.utils import create_access_token
from .schema import LoginRequestData, UserCreate
from .engine import BasicAuthEngine

# add views heres
logger = getLogger(__name__)

router = APIRouter()


@router.post("/login", name="basic_login")
async def log_in(data: LoginRequestData, response: Response, db=Depends(get_db)):
    user = await BasicAuthEngine(db).authenticate(data)
    if user is None:
        logger.warning(f"Failed login attempt for username: {data.username}")
        raise exceptions.HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    role = "admin" if user.is_superuser else "base"
    token = create_access_token(
        subject=str(user.user_id), username=user.username, user_role=role
    )

    response.set_cookie(
        key="Access-Token",
        value=token,
        secure=True,
        httponly=True,
        samesite="lax",
    )
    return {"message": "Login successfully", "role": role}


@router.post("/signup")
async def sign_up(
    data: UserCreate,
    response: Response,
    db=Depends(get_db),
):
    try:
        user = await BasicAuthEngine(db).sign_up(data.model_dump())
        role = "admin" if user["is_superuser"] else "base"
        
        token = create_access_token(
            subject=str(user["user_id"]), 
            username=user["username"], 
            user_role=role
        )
        
        response.set_cookie(
            key="Access-Token",
            value=token,
            secure=True,
            httponly=True,
            samesite="lax",
            max_age=60 * 15 # TODO: do not hard code this
        )

        logger.info(f"User {user['username']} successfully authenticated as {role}")
        
        return {
            "message": "Sign Up successful",
            "access_token": token,
            "user_id": user["user_id"],
            "username": user["username"],
            "role": role
        }

    except Exception as e:
        logger.error(f"[ERROR]: authenticating user: {str(e)}")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"error": str(e)}
        )