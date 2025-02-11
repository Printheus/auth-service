from sqlalchemy.ext.asyncio import AsyncSession
import sqlalchemy as sa

from .models import User, uuid
from .utils import bcrypt_hasher
from . import schema


class UserController:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def retrieve_by_id(self, user_id: str):
        query = sa.select(User).where(User.user_id == uuid.UUID(user_id))
        result = await self.db.scalars(query)
        return result.first()

    async def create(self, user:schema.UserCreate):
        user.password = bcrypt_hasher(user.password).decode()
        user = User(**user.model_dump())
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def retrieve_by_username(username:str):
        ...