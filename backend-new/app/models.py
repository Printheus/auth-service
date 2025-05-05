from sqlalchemy.orm import Mapped, mapped_column
import sqlalchemy as sa
import uuid, datetime
from .database import Base
    

class User(Base):
    __tablename__ = "Users"

    password: Mapped[str]
    username: Mapped[str] = mapped_column(unique=True)
    phone: Mapped[str | None] = mapped_column(nullable=True, unique=True, default=None)
    email: Mapped[str | None] = mapped_column(nullable=True, unique=True, default=None)
    is_active: Mapped[bool] = mapped_column(default=True)
    first_name: Mapped[str|None] = mapped_column(default="")
    last_name: Mapped[str|None] = mapped_column(default="")
    is_staff: Mapped[bool] = mapped_column(default=False)
    date_joined: Mapped[datetime.datetime] = mapped_column(sa.DateTime, default=None)
    is_superuser: Mapped[bool] = mapped_column(default=False)
    user_id: Mapped[str] = mapped_column(
        sa.types.UUID,
        primary_key=True,
        unique=True,
        nullable=False,
        default_factory=uuid.uuid4,
        index=True,
    )
