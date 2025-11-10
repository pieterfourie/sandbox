from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class User(BaseModel):
    name: str
    email: EmailStr
    age : int
    is_active: bool = True
    created_at: datetime = None

# Test with clean data

clean_data = {

    "name": "John Doe",
    "email": "example@gmail.com",
    "age" : 30,
}

user = User(**clean_data)

print(f"User created: {user.name}, Age: {user.age}, Email: {user.email}")
print(f"Model output: {user.model_dump()}")

# Messy data that still works

messy_data = {
    "name" : "Bob Smith",
    "email": "bob@company.com",
    "age" : "45", # String instead of int
    "is_active": "false", # String instead of bool
}

user = User(**messy_data)
print(f" Age type: {type(user.age)}")
print(f" Is_active type: {type(user.is_active)}")

