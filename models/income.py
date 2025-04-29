# Imports
from db.database import Base
from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey,Float
from sqlalchemy.orm import relationship

# Table
class DbIncome(Base):
    __tablename__ = 'incomes'

#  => Columns
    id = Column(Integer,primary_key=True,index=True)
    amount = Column(Float,nullable=False)
    date = Column(Date)
    source = Column(String)
    is_recurring = Column(Boolean,default=False)
# Foriegn Key
    user_id = Column(Integer,ForeignKey('users.id'))

# Relationships
    user = relationship('DbUser',back_populates='incomes')
