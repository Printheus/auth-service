from fastapi import Depends
from fastapi.routing import APIRouter
from auth_service.core.database import get_db
from .schema import LoginRequestData
from .engine import BasicAuthEngine

# add views heres

router = APIRouter()


@router.post("/login")
async def log_in(data: LoginRequestData, db=Depends(get_db)):
    usr = await BasicAuthEngine(db).authenticate(data)
    return data
