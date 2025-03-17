from pydantic import BaseModel, Field

class Product(BaseModel):
    """Product schema"""
    name: str = Field(..., alias="name")
    sales_amount: int = Field(..., alias="salesAmount")

class TopProductsResponse(BaseModel):
    """Response schema for Top Products API"""
    top_products: list[Product] = Field(..., alias="topProducts")
