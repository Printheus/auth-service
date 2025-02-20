from abc import ABC, abstractmethod
from .controllers import UserController, AsyncSession


class AbstractAuthEngine(ABC):
    def __init__(self, user_controller: UserController):
        self.user_controller = user_controller
        super().__init__()

    @abstractmethod
    async def authenticate(self): ...
    @abstractmethod
    async def is_acceptable(self) -> bool: ...
    @abstractmethod
    def is_valid(self) -> bool: ...
