import uuid

from sqlalchemy import Column, Date, DateTime, Float, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

from database import engine

Base = declarative_base()


class Delivery(Base):
    __tablename__ = "deliveries_delivery"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    freight_price = Column(Float(precision=2))
    partner_route_id = Column(UUID(as_uuid=True), nullable=True)
    modified = Column(DateTime)


Base.metadata.create_all(engine)
