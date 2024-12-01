from typing import Annotated
from pydantic import BaseModel, Field
from datetime import datetime
from .base import BaseClass

class TelegramUser(BaseModel,BaseClass):

    id: Annotated[int , Field(gt=0)]
    user_name: Annotated[str, Field(min_length=2, max_length=50)]

class User(BaseModel, BaseClass):

    id: Annotated[int , Field(gt=0)]
    first_name: Annotated[str, Field(min_length=2, max_length=50)]
    last_name: Annotated[str, Field(min_length=2, max_length=50)]
    phone: str
    email: str
    birthday: datetime

    # TODO: дописать валидацию для номера и email
    # TODO: посмотреть порядок наследования
