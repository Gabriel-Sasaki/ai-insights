from fastapi import APIRouter

from app.api.v1.endpoints.sales_insights import router as sales_insights_router
from app.api.v1.endpoints.top_products import router as top_products_router

router = APIRouter()

router.include_router(
    sales_insights_router,
    tags=["Sales Insights"]
)

router.include_router(
    top_products_router,
    tags=["Top Products"]
)
