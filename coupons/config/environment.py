

from typing import Callable
from dotenv import load_dotenv
from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    DATABASE_URL: PostgresDsn = (
        "postgresql+asyncpg://admin:admin@localhost:5432/fastapi"
    )
    WEB_APP_TITLE: str = "Coupons API"
    WEB_APP_DESCRIPTION: str = "Coupons backend api "
    WEB_APP_VERSION: str = "0.1.0"
    WEB_SERVER_HOST: str = "localhost"
    WEB_SERVER_PORT: int = 8000
    WEB_SERVER_RELOAD: bool = True
    ORB_URL: str = "https://orb.api.staging.binamik.com.br"

def _configure_initial_settings() -> Callable[[], Settings]:
    load_dotenv()
    settings = Settings()

    def fn() -> Settings:
        return settings

    return fn

get_settings = _configure_initial_settings()