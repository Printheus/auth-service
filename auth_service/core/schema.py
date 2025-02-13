from typing import Optional, Self
from pydantic import BaseModel, model_validator, EmailStr


class UserCreate(BaseModel):
    password: str
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None

    @model_validator(mode="after")
    def check_username(self) -> Self:
        if not (self.email or self.phone or self.username):
            raise ValueError("username should provide")
        if self.username is None:
            self.username = self.email or self.phone
        return self