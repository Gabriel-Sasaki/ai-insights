from fastapi import Depends, APIRouter

from sqlalchemy.orm import Session

from app.db.session import get_db

router = APIRouter()

@router.get("/sales-insights?question={question}")
async def get_sales_insights(
    question: str,
    db: Session = Depends(get_db)
):
    pass
