from logging import getLogger
from fastapi import exceptions, status
from bcrypt import checkpw
from auth_service.core.engine import AbstractAuthEngine
from auth_service.core.models import User

logger = getLogger(__name__)


class BasicAuthEngine(AbstractAuthEngine):
    async def authenticate(self, data) -> User | None:

        user = await self.user_controller.retrieve_by_username(data.username)
        if (user is None) or (
            not checkpw(data.password.encode(), user.password.encode())
        ):
            return None
        if not user.is_active:
            raise exceptions.HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="user is not active"
            )
        return user

    async def sign_up(self, data: dict) -> User:
        logger.info(f"\nProcessing sign_up request")
        user = await self.user_controller.create(data)
        return user.__dict__
