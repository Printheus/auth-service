from fastapi import exceptions, status
from auth_service.core.engine import AbstractAuthEngine
from auth_service.core.models import User
from bcrypt import checkpw
from .schema import LoginRequestData


class BasicAuthEngine(AbstractAuthEngine):
    async def authenticate(self, data: LoginRequestData):
        user = await self.user_controller.retrieve_by_username(data.username)
        if user is None or checkpw(data.password.encode(), user.password.encode()):
            raise exceptions.HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="not found."
            )
        return user

    def is_valid(self):
        return super().is_valid()

    def is_acceptable(self, user: User):
        # check user type and type available logins
        # check if user is active
        return super().is_acceptable()
