from fastapi.applications import FastAPI

from api.routers.coupon.v1 import controllers as coupon_controller

def register_routers(app: FastAPI) -> FastAPI:
    app.include_router(coupon_controller.router, prefix="/api/v1")

    return app