from db.base_class import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

class Item(Base):
    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    
    
    
    #RELATIONS
    stats = relationship("Item_stats", back_populates="user")
    