

from typing import Callable
from dotenv import load_dotenv
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')
    DATABASE_URL: PostgresDsn = (
        "postgresql://postgres:password@localhost:5432/coupons_develop"
    )
    WEB_APP_TITLE: str = "Coupons API"
    WEB_APP_DESCRIPTION: str = "Coupons backend api "
    WEB_APP_VERSION: str = "0.1.0"
    WEB_SERVER_HOST: str = "127.0.0.1"
    WEB_SERVER_PORT: int = 8000
    WEB_SERVER_RELOAD: bool = False
    ORB_URL: str = "http://localhost:8080"

def _configure_initial_settings() -> Callable[[], Settings]:
    load_dotenv()
    settings = Settings()

    def fn() -> Settings:
        return settings

    return fn

get_settings = _configure_initial_settings()
