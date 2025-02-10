from core.config_manager import conf
from fastapi import FastAPI, Depends
from core.models import Base
from core.database import engine, get_db
from core.controllers import UserController
from core.schema import UserCreate
from core.utils import bcrypt_hasher

async def create_all():
    async with engine.begin() as con:
        await con.run_sync(Base.metadata.create_all)


app = FastAPI()
app.add_event_handler("startup", create_all)


@app.post("/")
async def index(user:UserCreate, db=Depends(get_db)):
    user.password = bcrypt_hasher(user.password).decode()
    user = await UserController(db).create(user)
    return user.user_id
    user = await UserController(db).create(user)
    return user
