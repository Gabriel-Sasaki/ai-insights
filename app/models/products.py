from sqlalchemy import Column, Integer, String, Numeric

from app.db.base import Base

class Product(Base):
    """Product model representing a product record in the database.
    
    Attributes:
        id: Primary key.
        sku: Product SKU (non-null and unique).
        name: Product name (non-null).
        category: Product category.
        price: Product price as NUMERIC(10, 2) (non-null).
    
    Methods:
        as_dict: Converts the Product instance to a dictionary.
    """

    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String(50), unique=True, nullable=False, index=True)
    name = Column(String(255), nullable=False, index=True)
    category = Column(String(100), index=True)
    price = Column(Numeric(10, 2), index=True)

    def as_dict(self):
        """Converts the Product instance to a dictionary."""
        return {
            "id": self.id,
            "sku": self.sku,
            "name": self.name,
            "category": self.category,
            "price": float(self.price),
        }
