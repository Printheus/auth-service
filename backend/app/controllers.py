from fastapi.exceptions import HTTPException

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
import sqlalchemy as sa

from .models import User, uuid
from .utils import bcrypt_hasher

from datetime import datetime, timezone

class UserController:
    def __init__(self, db: Session):
        self.db = db

    def retrieve_by_id(self, user_id: str):
        query = sa.select(User).where(User.user_id == uuid.UUID(user_id))
        result = self.db.scalars(query)
        return result.first()

    def create(self, user: dict[str:str]) -> User:
        user["password"] = bcrypt_hasher(user["password"]).decode()
        user = User(**user, date_joined=datetime.now(timezone.utc))
        self.db.add(user)
        try:
            self.db.commit()
            self.db.refresh(user)
        except IntegrityError as e:
            raise HTTPException(
                status_code=400, detail="duplicated in username or email or phone"
            )
        return user

    def retrieve_by_username(self, username: str) -> User | None:
        query = sa.select(User).where(User.username == username)
        result = self.db.scalars(query)
        return result.first()