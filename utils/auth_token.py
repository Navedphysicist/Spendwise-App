from fastapi import HTTPException ,status,Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt,JWTError
from datetime import datetime,timezone,timedelta
from db.database import get_db
from sqlalchemy.orm import Session
from models.user import DbUser


SECRET_KEY = 'SECRET'

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/login')


def create_token(data:dict):
    to_encode = data.copy()
    expire_time = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({'exp':expire_time})
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm='HS256')
    return encoded_jwt


def get_current_user(token:str = Depends(oauth2_scheme),db:Session = Depends(get_db)):

    payload = jwt.decode(token,SECRET_KEY,algorithms=['HS256'])
    username = payload.get('sub')
    user = db.query(DbUser).filter(DbUser.username == username).first()
    return user
