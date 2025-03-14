import uvicorn

from fastapi import FastAPI

from app.db.base import Base
from app.db.session import engine
from app.api.v1.router import router as api_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sales Insights API",
    description="An API to get insights about sales data using OpenAI's GPT-4o-mini and "\
                "SQLAlchemy. Created for a technical assessment by Gabriel Pinto Sasaki.",
    version="0.1"
)

app.include_router(api_router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
