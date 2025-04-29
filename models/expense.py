# Imports
from db.database import Base
from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey,Float
from sqlalchemy.orm import relationship

# Table
class DbExpense(Base):
    __tablename__ = 'expenses'

#  => Columns
    id = Column(Integer,primary_key=True,index=True)
    amount = Column(Float,nullable=False)
    date = Column(Date)
    category = Column(String)
    is_recurring = Column(Boolean,default=False)
# Foriegn Key
    user_id = Column(Integer,ForeignKey('users.id'))

# Relationships
    user = relationship('DbUser',back_populates='expenses')

