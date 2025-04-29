from fastapi import FastAPI
from db.database import Base,engine

from models.user import DbUser
from models.income import DbIncome
from models.expense import DbExpense


from routers import auth,income,expense


app = FastAPI()


app.include_router(auth.router)
app.include_router(income.router)
app.include_router(expense.router)




Base.metadata.create_all(bind=engine)


@app.get('/')
def root():
    return {
        'message' : "Welcome to Spendwise App"
    }

# source my_env/bin/activate