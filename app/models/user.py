from sqlalchemy import Column, Integer, String, Float, Boolean
from app.database import Base

class User(Base): # Herencia
    __tablename__ = "users"
    
    id = Column(Integer, primary_key= True, index= True)
    name = Column(String)
    phone = Column(String, unique= True)
    password_hash = Column(String)
    amount = Column(Float, default=0)


