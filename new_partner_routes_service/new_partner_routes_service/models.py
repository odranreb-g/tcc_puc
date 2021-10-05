import uuid

from sqlalchemy import Column, DateTime, Float, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

from database import engine

Base = declarative_base()


class PartnerRoute(Base):
    __tablename__ = "deliveries_partnerroute"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    start_place = Column(String(50))
    finish_place = Column(String(50))
    price = Column(Float(precision=2))
    status = Column(String(10))
    partner_id = Column(UUID(as_uuid=True), nullable=True)
    created = Column(DateTime)
    modified = Column(DateTime)


Base.metadata.create_all(engine)
