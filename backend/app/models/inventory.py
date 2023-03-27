from db.base_class import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Inventory(Base):
    id = Column(Integer, primary_key=True, unique=True, index=True)
    item = Column(Integer, ForeignKey("item.id", ondelete="CASCADE"))
    backpack = Column(Integer, ForeignKey("backpack.id", ondelete="CASCADE"))