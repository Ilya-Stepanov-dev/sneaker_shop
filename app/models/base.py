from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from db_helper import Base

class BaseClass():

    date_creation: datetime
    date_update: datetime

    # TODO Сделать базовый класс для наследования 