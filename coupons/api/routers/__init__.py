from fastapi.applications import FastAPI

from api.routers import application_controller
from api.routers.coupon.v1 import controllers as coupon_controller

def register_routers(app: FastAPI) -> FastAPI:
    app.include_router(application_controller.router)
    app.include_router(coupon_controller.router, prefix="/api/v1")
    return app