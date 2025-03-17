from pydantic import BaseModel, Field

class SalesInsightsResponse(BaseModel):
    """Response schema for Sales Insights API"""
    ai_answer: str = Field(..., alias="aiAnswer")
