from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class autor(BaseModel):
    id: Optional[int]
    FIO : str


class book(BaseModel):
    id: Optional[int]
    name: str
    autor_id: str
    year_of_publication: Optional[datetime]
    count_book: Optional[int]


class reader (BaseModel):
    id: Optional[int]
    FIO: str
    Address: str
    phone: str


class staff(BaseModel):
    id: Optional[int]
    FIO_S: str
    phone_S: int

class issuance(BaseModel):
    id: Optional[int]
    book_id: int
    staff_id: int
    date_issuance: Optional[datetime]
    date_delivery: Optional[datetime]