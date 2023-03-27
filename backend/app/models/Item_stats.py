from db.base_class import Base
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

class Item_stats(Base):
    id = Column(Integer, primary_key=True, unique=True, index=True)
    attack = Column(Integer, nullable=True)
    defense = Column(Integer, nullable=True)