from typing import Annotated
# from annotated_types import Gt, Le, MaxLen, Date
from pydantic import BaseModel, Field
from datetime import datetime


class BaseUser(BaseModel):

    user_id: Annotated[int , Field(gt=0)]
    user_type: Annotated[int, Field(gt=0)]
    user_name: Annotated[str, Field(min_length=2, max_length=50)]
    data_registration: datetime
    last_activity: datetime


class TypeUser(BaseModel):

    type_user_id: Annotated[int, Field(gt=0)]
    type_name: Annotated[str, Field(min_length=2, max_length=50)]


class User(BaseModel):

    user_id: Annotated[int , Field(gt=0)]
    first_name: Annotated[str, Field(min_length=2, max_length=50)]
    last_name: Annotated[str, Field(min_length=2, max_length=50)]
    phone: str
    email: str
    birthday: datetime

    # TODO: дописать валидацию для номера и email


