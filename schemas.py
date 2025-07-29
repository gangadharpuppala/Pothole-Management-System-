from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum

class Role(str, Enum):
    public = "public"
    staff = "staff"
    admin = "admin"

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    role: Role
    class Config:
        orm_mode = True

class PotholeReportCreate(BaseModel):
    description: str
    latitude: float
    longitude: float

class PotholeReportOut(BaseModel):
    id: int
    description: str
    status: str
    class Config:
        orm_mode = True

