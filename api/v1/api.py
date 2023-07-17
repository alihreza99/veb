
from fastapi import APIRouter
from .endpoints import (user,kala,hi)

api_router = APIRouter()

api_router.include_router(
        user.router,
        prefix="/user",
        tags=["User"]
    )

api_router.include_router(
        kala.router,
        prefix="/kala",
        tags=["Kala"]
    )


