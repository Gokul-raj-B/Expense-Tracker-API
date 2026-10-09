from pydantic import BaseModel, EmailStr, Field
from datetime import date
from decimal import Decimal

# User Registration
class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)

# User Response
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    model_config = {"from_attributes": True}

# User Login
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Add Expense
class ExpenseCreate(BaseModel):
    title: str = Field(max_length=100)
    amount: Decimal = Field(gt=0, max_digits=10, decimal_places=2)
    category: str = Field(max_length=50)
    date: date
    payment_method: str = Field(max_length=30)

# Expense Response
class ExpenseResponse(BaseModel):
    id: int
    title: str
    amount: Decimal
    category: str
    date: date
    payment_method: str
    user_id: int

    model_config = {"from_attributes": True}