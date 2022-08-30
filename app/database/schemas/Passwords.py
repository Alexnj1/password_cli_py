from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base, engine

# table class for passwords

class Password(Base):
  __tablename__ = "Passwords_3"
  id = Column(Integer, primary_key = True)
  password = Column(String(100), nullable = False)
  matches = Column(String(100), nullable = False)
  belongs_to = Column(Integer, ForeignKey("Users_1.id"), nullable = False)
  created_at = Column(DateTime, default=datetime.now)
  updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

  user = relationship('User')

Base.metadata.create_all(engine)