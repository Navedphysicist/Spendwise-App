# Pydantic models to validate Request Data and Response Data
# Imports
from pydantic import BaseModel
from datetime import date as date_type
from typing import Optional


# Pydantic models for Request
class IncomeBase(BaseModel):
    amount : float
    date : date_type
    source : str
    is_recurring : bool = False

class IncomeUpdate(BaseModel):
    amount : Optional[float] = None
    date : Optional[date_type]= None
    source : Optional[str] = None
    is_recurring : Optional[bool] = None


# Pydantic models for Response
class IncomeDisplay(IncomeBase):
    id : int
    user_id : int

    class Config:
        from_attributes = True
