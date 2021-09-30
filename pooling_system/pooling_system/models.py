import uuid

from sqlalchemy import Column, Date, DateTime, Float, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_serializer import SerializerMixin

from database import engine

Base = declarative_base()


class Delivery(Base, SerializerMixin):
    __tablename__ = "deliveries_delivery"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    sender_name = Column(String(100))
    sender_address = Column(String(100))
    sender_city = Column(String(100))
    sender_postal_code = Column(String(100))

    receiver_name = Column(String(100))
    receiver_address = Column(String(100))
    receiver_city = Column(String(100))
    receiver_postal_code = Column(String(100))

    freight_price = Column(Float(precision=2))

    expected_delivery_date = Column(Date)
    delivery_date = Column(Date)

    type = Column(String(9))
    status = Column(String(10))
    partner_id = Column(UUID(as_uuid=True), nullable=True)

    created = Column(DateTime)
    modified = Column(DateTime)

    def to_dict(self, *args, **kwargs):
        dict = super().to_dict()

        dict["delivery_entry_created"] = dict["created"]
        dict["delivery_entry_modified"] = dict["modified"]

        del dict["created"]
        del dict["modified"]

        return dict


Base.metadata.create_all(engine)
