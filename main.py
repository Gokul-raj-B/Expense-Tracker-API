from fastapi import FastAPI
from routers.users import router as users_router
from routers.expenses import router as expenses_router

app = FastAPI(title="Expense Tracker API")

app.include_router(users_router)
app.include_router(expenses_router)

@app.get("/")
def home():
    return {"message": "Expense Tracker API is running"}