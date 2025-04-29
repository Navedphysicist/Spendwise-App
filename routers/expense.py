# Expense Routes
# Import
from fastapi import APIRouter,Depends
from schemas.expense import ExpenseBase,ExpenseUpdate, ExpenseDisplay
from db.database import get_db
from sqlalchemy.orm import Session
from utils.auth_token import get_current_user
from models.expense import DbExpense
from typing import Optional



router = APIRouter(
    prefix='/expenses',
    tags=['Expense']
)



# Create Expense : Authenticated : [POST]
@router.post('/',response_model=ExpenseDisplay)
def create_expense(expense : ExpenseBase,db:Session = Depends(get_db),current_user = Depends(get_current_user)):
    
    expense_data = DbExpense(**expense.model_dump(),user_id=current_user.id)

    db.add(expense_data)
    db.commit()
    db.refresh(expense_data)
    return expense_data


# Get Expense : Authenticated : [GET]
@router.get('/')
def get_expense(category:Optional[str]= None, db:Session = Depends(get_db),current_user = Depends(get_current_user)):

    query = db.query(DbExpense).filter(DbExpense.user_id == current_user.id)

    if category:
       query =  query.filter(DbExpense.category.ilike(f"%{category}%"))

    return query.all()



# Update Expense : Authenticated : [PATCH]
@router.patch('/{expense_id}')
def update_expense(expense_id:int, expense:ExpenseUpdate,db:Session = Depends(get_db),current_user = Depends(get_current_user)):

    expense_data = db.query(DbExpense).filter(DbExpense.id == expense_id).first()

    expense_update = expense.model_dump(exclude_unset=True)

    for key,value in expense_update.items():
        setattr(expense_data,key,value)


    db.commit()
    db.refresh(expense_data)
    return expense_data



# Delete Expense : Authenticated : [Delete]
@router.delete('/{expense_id}')
def update_expense(expense_id:int,db:Session = Depends(get_db),current_user = Depends(get_current_user)):

    expense_data = db.query(DbExpense).filter(DbExpense.id == expense_id).first()

    db.delete(expense_data)
    db.commit()
    return {
        'message': 'Deleted Successfully'
    }