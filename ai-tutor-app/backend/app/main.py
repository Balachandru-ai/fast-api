from fastapi import FastAPI

from app.database.db import engine

from app.database.base import Base

from app.api.auth_routes import router as auth_router
from app.api.user_routes import router as user_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Tutor API",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(user_router)


@app.get("/")
def home():
    return {
        "message": "AI Tutor API Running"
    }