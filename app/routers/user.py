from fastapi import APIRouter
from datetime import datetime

from core_sсhemas.user import BaseUser

router = APIRouter(
    prefix='/users',
    tags=['users'],
)

# users = [ BaseUser(user_id=1,
#                 user_name='Ilya',
#                 user_type=1,
#                 data_registration = datetime.now(),
#                 last_activity = datetime.now()),

#     BaseUser(user_id=2,
#                 user_name='Nicola',
#                 user_type=1,
#                 data_registration = datetime.now(),
#                 last_activity = datetime.now())
# ]

# print(users[1])

@router.get('/')
async def get_user(user_id: int) -> BaseUser:
    pass
    # return users[user_id -1]