from datetime import date

from pydantic import BaseModel, EmailStr

from src.schemas.users import User


class ContactBase(BaseModel):
    email: EmailStr


class ContactCreate(ContactBase):
    first_name: str
    last_name: str
    phone: str
    birth_date: date
    bio: str


class Contact(ContactBase):
    id: int
    first_name: str
    last_name: str
    phone: str
    birth_date: date
    bio: str
    owner: User

    class Config:
        from_attributes = True
