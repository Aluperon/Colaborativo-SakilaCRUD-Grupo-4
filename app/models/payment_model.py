from sqlalchemy import Column, Integer, ForeignKey, Numeric, DateTime
from app.core.database import Base

class Payment(Base):
    __tablename__ = "payment"

    payment_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customer.customer_id"))
    staff_id = Column(Integer, ForeignKey("staff.staff_id"))
    rental_id = Column(Integer, ForeignKey("rental.rental_id"))
    amount = Column(Numeric(5, 2))
    payment_date = Column(DateTime)
    last_update = Column(DateTime)
