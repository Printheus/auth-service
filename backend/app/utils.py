import bcrypt
import jwt
from jwt.exceptions import InvalidTokenError, ExpiredSignatureError
from datetime import datetime, timedelta, timezone

from .settings import settings


def verify_token(token: str) -> dict:
    """
    Verify and decode a JWT access token.

    Args:
        token (str): The JWT token to verify.

    Returns:
        dict: Decoded token payload if valid.

    Raises:
        ExpiredSignatureError: If the token has expired.
        InvalidTokenError: If the token is invalid or cannot be decoded.
    """
    try:
        payload = jwt.decode(
            token,
            settings.public_key,
            algorithms=["RS256"],
            options={
                "verify_exp": True,
                "verify_iat": True,
                "verify_nbf": True,
            },
        )
        return payload
    except ExpiredSignatureError:
        raise ExpiredSignatureError("Token has expired")
    except InvalidTokenError as e:
        raise InvalidTokenError(f"Invalid token: {str(e)}")


def create_token(
    payload:dict, expires_delta: timedelta | None = None
) -> str:
    """
    Generate a JWT access token with specified claims.

    Args:
        payload (dict): Payload of Token
        expires_delta (timedelta | None): Optional expiration time delta

    Returns:
        str: Encoded JWT token
    """
    current_time = datetime.now(timezone.utc)
    expiration_time = current_time + (
        expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE)
    )

    payload = {
        **payload,
        "exp": expiration_time,
        "iat": current_time,
        "nbf": current_time,
    }

    return jwt.encode(payload, settings.private_key, algorithm="RS256")


def bcrypt_hasher(passwd: str) -> bytes:
    salt = bcrypt.gensalt()
    passwd = bcrypt.hashpw(passwd.encode(), salt)
    return passwd
