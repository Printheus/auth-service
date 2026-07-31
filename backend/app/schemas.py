import re
from typing import Optional, Self
from pydantic import BaseModel, EmailStr, field_validator, model_validator


class LoginRequestData(BaseModel):

    username: str
    password: str

class UserCreate(BaseModel):
    """
    Model for creating a new user with validation for required fields.
    """
    password: str
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None

    @model_validator(mode="after")
    def validate_username(self) -> Self:
        """
        Ensure at least one of email, phone, or username is provided.
        If username is not provided, set it to email or phone.
        """
        if not any([self.email, self.phone, self.username]):
            raise ValueError("At least one of email, phone, or username must be provided")
        
        if self.username is None:
            self.username = self.email or self.phone
        
        return self

    @field_validator("password")
    def validate_password(cls, value: str) -> str:
        """
        Validate password strength.
        """
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if not re.search(r"[A-Z]", value):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r"[a-z]", value):
            raise ValueError("Password must contain at least one lowercase letter")
        if not re.search(r"\d", value):
            raise ValueError("Password must contain at least one digit")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
            raise ValueError("Password must contain at least one special character")
        return value
    
    @field_validator("phone")
    def validate_phone(cls, value: Optional[str]) -> Optional[str]:
        """
        Validate phone number format (if provided).
        """
        if value is not None:
            # if not re.match(r"^\+?[1-9]\d{1,14}$", value):
            if not re.match(r"((\+98|0)9\d{9})", value):
                raise ValueError("Phone number must be in iran cellphones format")
        return value
    
    
