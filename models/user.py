# Imports
from db.database import Base
from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey,Float
from sqlalchemy.orm import relationship


class DbUser(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index= True)
    username = Column(String, unique=True)
    password = Column(String)

# Relationships
    incomes = relationship('DbIncome',back_populates='user')    
    expenses = relationship('DbExpense',back_populates='user')    