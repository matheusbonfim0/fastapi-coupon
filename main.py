from fastapi import FastAPI, APIRouter
from routes import user_router

app = FastAPI()
router = APIRouter()

app.include_router(prefix='/first', router=router)
app.include_router(user_router)
