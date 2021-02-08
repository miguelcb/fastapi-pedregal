from sqlalchemy import Boolean, Column, Integer, String, Date
from .database import Base


class Person(Base):
    __tablename__ = "persons"

    document_id = Column(Integer, primary_key=True, unique=True, index=True)
    first_name = Column(String(50), index=True)
    last_name = Column(String(50), index=True)
    birthdate = Column(Date)
    is_active = Column(Boolean, default=True)