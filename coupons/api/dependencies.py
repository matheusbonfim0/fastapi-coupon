import httpx
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from coupons.config.environment import get_settings
from coupons.domain.accounts.entities import User

settings = get_settings()
authorization = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(authorization),
) -> User:
    headers = {'Authorization': f'Bearer {credentials.credentials}'}
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.post(f'{settings.ORB_URL}/login', headers=headers)
            response.raise_for_status()
            user_json = response.json()['user']
    except (httpx.HTTPError, KeyError, ValueError) as exc:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail='Token inválido.') from exc
    if not user_json.get('company'):
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail='Usuário sem empresa.')
    return User(
        id=user_json['id'], name=user_json['name'], email=user_json['email'],
        company_id=user_json['company']['id'], roles=user_json['company']['roles'],
    )
