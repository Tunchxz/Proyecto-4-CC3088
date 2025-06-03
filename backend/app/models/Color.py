from sqlalchemy import Column, Integer, String
from db import Base

class Color(Base):
    __tablename__ = 'color'
    id = Column(Integer, primary_key=True)
    color_name = Column(String(16), unique=True, nullable=False)