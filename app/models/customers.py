from sqlalchemy import Column, Integer, String, TIMESTAMP

from app.db.base import Base

class Customer(Base):
    """Customer model representing a customer record in the database.
    
    Attributes:
        id: Primary key.
        name: Customer name (non-null).
        email: Customer email (non-null and unique).
        created_at: Date and time the customer was created (defaults to current timestamp).

    Methods:
        as_dict: Converts the Customer instance to a dictionary.
    """

    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    created_at = Column(TIMESTAMP)

    def as_dict(self):
        """Converts the Customer instance to a dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "created_at": self.created_at,
        }
