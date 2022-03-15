import requests
from fastapi import Depends
from fastapi.exceptions import HTTPException
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.security.http import HTTPBearer

from coupons.config.environment import get_settings
from coupons.domain.accounts.entities import User

settings = get_settings()
authorization = HTTPBearer()

async def get_current_user(
    authorization: HTTPAuthorizationCredentials = Depends(authorization),
) -> User:
    headers = {"Authorization": f'Bearer {authorization.credentials}'}
    response = requests.post(f"{settings.ORB_URL}/login", headers=headers)

    if response.status_code != 200:
        raise HTTPException(status_code=401)

    user_json = response.json()["user"]
    if not user_json.get("company"):
        raise HTTPException(status_code=403)
    return User(
        id=user_json["id"],
        name=user_json["name"],
        email=user_json["email"],
        company_id=user_json["company"]["id"],
        roles=user_json["company"]["roles"],
    )