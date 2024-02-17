
from .database import Base

from sqlalchemy import (
    Column,
    String,
    Integer,
    TIMESTAMP,
    text
)
from datetime import datetime

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))