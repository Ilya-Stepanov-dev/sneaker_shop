from db_helper import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from .base import BaseClass

class TelegramUser(Base, BaseClass):
    __tablename__ = 'telegram_users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str] = mapped_column(nullable=False)
    data_registration: Mapped[str] = mapped_column(nullable=False)
    last_activity: Mapped[str] = mapped_column(nullable=False)


class User(Base, BaseClass):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name : Mapped[str] = mapped_column(nullable=False)
    phone: Mapped[str] = mapped_column(unique=True, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    birthday: Mapped[str] = mapped_column(nullable=False)
    is_superuser: Mapped[bool] = mapped_column(nullable=False, default=False)
    telegram_user_id: Mapped[int] = mapped_column(ForeignKey('telegram_users.id'))

    telegram_user: Mapped[TelegramUser] = relationship(back_populates='users')