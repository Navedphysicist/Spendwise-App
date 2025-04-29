# Income Routes
# Import
from fastapi import APIRouter,Depends
from schemas.income import IncomeBase,IncomeUpdate, IncomeDisplay
from db.database import get_db
from sqlalchemy.orm import Session
from utils.auth_token import get_current_user
from models.income import DbIncome
from typing import Optional



router = APIRouter(
    prefix='/incomes',
    tags=['Income']
)




# Create Income : Authenticated : [POST]
@router.post('/',response_model=IncomeDisplay)
def create_income(income : IncomeBase,db:Session = Depends(get_db),current_user = Depends(get_current_user)):
    
    income_data = DbIncome(**income.model_dump(),user_id=current_user.id)

    db.add(income_data)
    db.commit()
    db.refresh(income_data)
    return income_data


# Get Income : Authenticated : [GET]
@router.get('/')
def get_income(source:Optional[str]= None, db:Session = Depends(get_db),current_user = Depends(get_current_user)):

    query = db.query(DbIncome).filter(DbIncome.user_id == current_user.id)

    if source:
       query =  query.filter(DbIncome.source.ilike(f"%{source}%"))

    return query.all()



# Update Income : Authenticated : [PATCH]
@router.patch('/{income_id}')
def update_income(income_id:int, income:IncomeUpdate,db:Session = Depends(get_db),current_user = Depends(get_current_user)):

    income_data = db.query(DbIncome).filter(DbIncome.id == income_id).first()

    # if income.amount is not None:
    #     income_data.amount = income.amount
    # if income.source is not None:
    #     income_data.source = income.source
    # if income.date is not None:
    #     income_data.date = income.date
    # if income.is_recurring is not None:
    #     income_data.is_recurring = income.is_recurring

    income_update = income.model_dump(exclude_unset=True)

    for key,value in income_update.items():
        setattr(income_data,key,value)


    db.commit()
    db.refresh(income_data)
    return income_data



# Delete Income : Authenticated : [Delete]
@router.delete('/{income_id}')
def update_income(income_id:int,db:Session = Depends(get_db),current_user = Depends(get_current_user)):

    income_data = db.query(DbIncome).filter(DbIncome.id == income_id).first()

    db.delete(income_data)
    db.commit()
    return {
        'message': 'Deleted Successfully'
    }