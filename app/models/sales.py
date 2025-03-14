from sqlalchemy import Column, Integer, Numeric, TIMESTAMP, ForeignKey

from app.db.base import Base

class Sale(Base):
    """Sale model representing a sale record in the database.

    Attributes:
        id: Primary key.
        product_id: Foreign key referencing the products table.
        customer_id: Foreign key referencing the customers table.
        quantity: Quantity sold (non-null).
        total_amount: Total sale amount as NUMERIC(10, 2) (non-null).
        sale_date: Date and time of the sale (non-null).
    
    Methods:
        as_dict: Converts the Sale instance to a dictionary.
    """

    __tablename__ = "sales"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    customer_id = Column(Integer, ForeignKey("customers.id"))
    quantity = Column(Integer, nullable=False)
    total_amount = Column(Numeric(10, 2), nullable=False)
    sale_date = Column(TIMESTAMP, nullable=False)

    def as_dict(self):
        """Converts the Sale instance to a dictionary."""
        return {
            "id": self.id,
            "product_id": self.product_id,
            "customer_id": self.customer_id,
            "quantity": self.quantity,
            "total_amount": float(self.total_amount),
            "sale_date": self.sale_date,
        }
