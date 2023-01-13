from fastapi import APIRouter

from api.controllers.example import example_router

router = APIRouter()
router.include_router(example_router, prefix="/client", tags=["Example_Endpoint"])

__all__ = ["router"]
