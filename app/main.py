#uvicorn app.main:app --reload
from fastapi import FastAPI

from app.users.routers import router as users_router

app = FastAPI()



app.include_router(users_router)