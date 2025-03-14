from fastapi import Depends, APIRouter

from sqlalchemy.orm import Session

from app.db.session import get_db

router = APIRouter()

@router.get("/top-products")
async def get_top_products(
    db: Session = Depends(get_db)
):
    pass
