from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from infrastructure.database import DbConnect, Base

# Base = DbConnect.get_base_connection()
class Assesment(Base):
    __tablename__ = "assesment"

    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String)
    total_candidates = Column(Integer)
