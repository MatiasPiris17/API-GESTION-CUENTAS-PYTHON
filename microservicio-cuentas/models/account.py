from pydantic import BaseModel
from typing import Optional

class Account(BaseModel):
    id: Optional[str]
    name: Optional[str]
    email: str
    dni: str
    money: int

def account_schema(account) -> dict: 
    name = account.get("name", "")
    email = account.get("email")
    dni = account.get("dni")
    money = account.get("money")

    return {
            "name": name,
            "email": email,
            "dni": dni,
            "money": money
    }


def accounts_schema(accounts) -> list:
    return [account_schema(account) for account in accounts]
