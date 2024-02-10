
from .database import Base

from sqlalchemy import (
    Column,
    String,
    Integer,
    DateTime
)
from datetime import datetime

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)