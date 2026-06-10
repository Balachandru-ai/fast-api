from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database.db import get_db

from app.schemas.user_schema import (
    UserCreate,
    UserLogin
)

from app.services.auth_service import (
    register_user,
    login_user
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(
        user: UserCreate,
        db: Session = Depends(get_db)
):

    result = register_user(
        user,
        db
    )

    if not result:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    return {
        "message": "User registered successfully"
    }


@router.post("/login")
def login(
        user: UserLogin,
        db: Session = Depends(get_db)
):

    token = login_user(
        user.email,
        user.password,
        db
    )

    if not token:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    return {
        "access_token": token,
        "token_type": "bearer"
    }