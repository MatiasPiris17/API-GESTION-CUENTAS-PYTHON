from pydantic import BaseModel
from typing import Optional

class Account(BaseModel):
    id: Optional[str]
    name: Optional[str]
    email: str
    dni: str
    money: int
