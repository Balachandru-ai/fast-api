from fastapi import APIRouter
from fastapi import Depends

from app.core.dependencies import (
    get_current_user
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/profile")
def profile(
        current_user=Depends(
            get_current_user
        )
):
    return current_user