from fastapi import APIRouter
from core_sсhemas.user import BaseUser

router = APIRouter(
    prefix='/users',
    tags=['users'],
)
@router.get('/')
async def get_user(user_id: int) -> BaseUser:
    pass