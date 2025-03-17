import datetime as dt

from fastapi import Depends, APIRouter

from sqlalchemy import select, func
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.products import Product
from app.models.sales import Sale
from app.schemas.top_products import TopProductsResponse

router = APIRouter()

@router.get("/top-products")
async def get_top_products(db: Session = Depends(get_db)) -> TopProductsResponse:
    """Get the top 5 products by sales amount in the current month."""
    start_of_month = dt.datetime.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    stmt = select(
        Product.name,
        func.sum(Sale.quantity).label("sales_amount")
    )\
        .join(Product, Sale.product_id == Product.id)\
        .group_by(Product.name)\
        .where(Sale.sale_date >= start_of_month)\
        .order_by(func.sum(Sale.quantity).desc())\
        .limit(5)
    result = db.execute(stmt)
    top_products = [{"product": prod, "sale_count": sale_count} for prod, sale_count in result]
    return TopProductsResponse(top_products=top_products)
