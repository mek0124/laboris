from sqlalchemy import Column, String, Integer, Boolean, DateTime, UUID
from datetime import datetime
from uuid import uuid4

from ..database.db import get_base


Base = get_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(
        UUID,
        primary_key = True,
        index = True,
        unique = True,
        default = lambda: uuid4()
    )

    employee_id = Column(
        Integer,
        index = True,
        unique = True,
    )

    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String)
    password = Column(String)

    created_at = Column(
        DateTime,
        index = True,
        default = lambda: datetime.now()
    )

    updated_at = Column(
        DateTime,
        index = True,
        default = lambda: datetime.now(),
        onupdate = lambda: datetime.now()
    )