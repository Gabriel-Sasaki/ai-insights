from pydantic import BaseModel, Field

class SalesInsightsRequest(BaseModel):
    """Request schema for Sales Insights API"""
    question: str = Field(..., alias="question")

class SalesInsightsResponse(BaseModel):
    """Response schema for Sales Insights API"""
    ai_answer: str = Field(..., alias="aiAnswer")
