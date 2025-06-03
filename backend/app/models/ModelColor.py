from sqlalchemy import Column, ForeignKey, Integer
from db import Base
from sqlalchemy.orm import relationship

class ModelColor(Base):
    __tablename__ = 'model_color'
    model_id = Column(Integer, ForeignKey("model.id"), primary_key=True)
    color_id = Column(Integer, ForeignKey("color.id"), primary_key=True)

    model = relationship("Model", back_populates="colors")