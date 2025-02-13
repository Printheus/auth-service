import bcrypt
import jwt
from datetime import datetime, timedelta, timezone
from .config_manager import conf


def bcrypt_hasher(passwd: str) -> bytes:
    salt = bcrypt.gensalt()
    passwd = bcrypt.hashpw(passwd.encode(), salt)
    return passwd


def create_access_token(
    subject: str, username: str, user_role: str, expires_delta: timedelta | None = None
) -> str:
    """
    Generate a JWT access token with specified claims.

    Args:
        subject (str): Subject identifier (typically user ID)
        username (str): User's full name
        user_role (str): User's authorization role
        expires_delta (timedelta | None): Optional expiration time delta

    Returns:
        str: Encoded JWT token
    """
    current_time = datetime.now(timezone.utc)
    expiration_time = current_time + (
        expires_delta or timedelta(minutes=conf.TOKEN_EXPIRE)
    )

    payload = {
        "sub": subject,
        "name": username,
        "role": user_role,
        "exp": expiration_time,
        "iat": current_time,
        "nbf": current_time,
    }

    return jwt.encode(payload, conf.private_key, algorithm="RS256")
