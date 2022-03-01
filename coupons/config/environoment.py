

from typing import Callable
from dotenv import load_dotenv
from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    DATABASE_URL: PostgresDsn = (
        "postgresql+asyncpg://admin:admin@localhost:5432/fastapi"
    )
    WEB_SERVER_HOST: str = "localhost"
    WEB_SERVER_PORT: int = 8000
    WEB_SERVER_RELOAD: bool = True

def _configure_initial_settings() -> Callable[[], Settings]:
    load_dotenv()
    settings = Settings()

    def fn() -> Settings:
        return Settings

    return fn

get_settings = _configure_initial_settings()