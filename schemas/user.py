# Pydantic models to validate Request Data and Response Data
# Imports
from pydantic import BaseModel



class UserBase(BaseModel):
    username : str
    password : str



class Token(BaseModel):
    access_token : str