from fastapi.applications import FastAPI
from toolz import pipe

from coupons.api.routers import register_routers as register_routers
from coupons.config.environment import Settings


def create_instance(settings: Settings) -> FastAPI:
    return FastAPI(
        title=settings.WEB_APP_TITLE,
        description=settings.WEB_APP_DESCRIPTION,
        version=settings.WEB_APP_VERSION,
    )

def init_app(settings: Settings) -> FastAPI:
    app: FastAPI = pipe(
        settings,
        create_instance,
        register_routers,
    )
    return app