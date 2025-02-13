from abc import ABC, abstractmethod
from .controllers import UserController, AsyncSession


class AbstractAuthEngine(ABC):
    def __init__(self, db: AsyncSession):
        self.user_controller = UserController(db)
        super().__init__()

    @abstractmethod
    async def authenticate(self): ...