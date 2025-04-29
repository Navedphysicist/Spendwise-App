from fastapi import APIRouter, Depends
from schemas.user import UserBase
from sqlalchemy.orm import Session
from db.database import get_db
from models.user import DbUser
from utils.auth_token import create_token
from utils.hash import hash_password
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)



# signup => Create User [POST]
@router.post('/')
def create_user(request : UserBase, db:Session = Depends(get_db)):
    user = DbUser(username = request.username, password=hash_password(request.password))

    db.add(user)
    db.commit()
    db.refresh(user)

    access_token = create_token({'sub':user.username})
    return {
        'access_token' : access_token
    }

    

# login => Get Token [POST]
@router.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends(),db:Session = Depends(get_db)):

    user = db.query(DbUser).filter(DbUser.username==request.username).first()

    access_token = create_token({'sub':user.username})
    return {
        'access_token' : access_token
    }
