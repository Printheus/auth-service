from pydantic import BaseModel


class LoginRequestData(BaseModel):
    username: str
    password: str
    