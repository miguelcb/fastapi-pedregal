from typing import List, Optional
from pydantic import BaseModel
from datetime import date


class PersonBase(BaseModel):    
    first_name: str
    last_name: str
    birthdate: date


class PersonCreate(PersonBase):
    document_id: int


class PersonUpdate(PersonBase):    
    is_active: bool


class PersonDelete:
    document_id: int


class Person(PersonBase):
    document_id: int
    is_active: bool    

    class Config:
        orm_mode = True
