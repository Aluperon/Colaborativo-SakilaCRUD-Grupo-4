from sqlalchemy import Column, Integer, ForeignKey, DateTime
from app.core.database import Base

class Rental(Base):
    __tablename__ = "rental"

    rental_id = Column(Integer, primary_key=True, index=True)
    rental_date = Column(DateTime)
    inventory_id = Column(Integer, ForeignKey("inventory.inventory_id"))
    customer_id = Column(Integer, ForeignKey("customer.customer_id"))
    return_date = Column(DateTime)
    staff_id = Column(Integer, ForeignKey("staff.staff_id"))
    last_update = Column(DateTime)
