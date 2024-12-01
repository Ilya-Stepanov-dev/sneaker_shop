from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, func

class BaseClass():

    date_creation: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    date_update: Mapped[datetime] = mapped_column(DateTime, onupdate=func.now())