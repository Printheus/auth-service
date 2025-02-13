from .database import Base
from sqlalchemy.orm import Mapped, mapped_column, foreign
import sqlalchemy as sa
import uuid


class User(Base):
    __tablename__ = "Users"

    password: Mapped[str]
    username: Mapped[str] = mapped_column(unique=True)
    phone: Mapped[str | None] = mapped_column(nullable=True, unique=True)
    email: Mapped[str | None] = mapped_column(nullable=True, unique=True)
    is_active: Mapped[bool] = mapped_column(default=True)
    is_admin: Mapped[bool] = mapped_column(default=False)
    user_id: Mapped[str] = mapped_column(
        sa.types.UUID,
        primary_key=True,
        unique=True,
        nullable=False,
        default_factory=uuid.uuid4,
        index=True,
    )
