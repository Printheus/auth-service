from sqlalchemy.ext.asyncio import AsyncSession
import sqlalchemy as sa

from .models import User
from . import schema


class UserController:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def retrieve_by_id(self, user_id: int):
        query = sa.select(User).where(User.user_id == user_id)
        result = await self.db.execute(query)
        return result.scalars().first()

    async def create(self, user:schema.UserCreate):
        # TODO: Hash password
        user = User(**user.dict())
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user