from fastapi import APIRouter
from datetime import datetime

from core_sсhemas.user import BaseUser

router = APIRouter(
    prefix='users',
    tags=['users'],
)

users = [ BaseUser(user_id=1,
                user_name='Ilya',
                user_type=1,
                data_registration = datetime.now(),
                last_activity = datetime.now()),

    BaseUser(user_id=2,
                user_name='Ilya',
                user_type=1,
                data_registration = datetime.now(),
                last_activity = datetime.now())
]

@router.get('{user_id}')
async def get_user() -> BaseUser:
    return users[users_id]