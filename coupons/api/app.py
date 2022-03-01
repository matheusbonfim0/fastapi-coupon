from fastapi.applications import FastAPI
from toolz import pipe

from coupons.api.routers import register_routers as register_routers


def init_app() -> FastAPI:
    app: FastAPI = pipe(
        register_routers,
    )
    return app