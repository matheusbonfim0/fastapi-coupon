from fastapi import HTTPException, APIRouter

from schemas import StandardOutput, UserCreateGift
from services import UserService

user_router = APIRouter(prefix='/user')

@user_router.post('/create_gift')
async def create_gift(user_input: UserCreateGift):
    try:
        await UserService.create_gift(
            name=user_input.name,
            expire=user_input.expire,
            percent=user_input.percent,
            quantity=user_input.quantity
            )
        return StandardOutput(message='Cupom criado com sucesso!')
    except Exception as error:
        raise HTTPException(400, detail=str(error))