from db.base_class import Base
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

class Role(Base):
    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String, nullable=False)
    