from pydantic import BaseModel
from typing import Optional


class Transfer(BaseModel):
    id: Optional[str]
    sender: str
    addressee: str
    transfer_cant: int


def transfer_schema(transfer): 
    sender = transfer.get("sender", "")
    addressee = transfer.get("addressee", "")
    transfer_cant = transfer.get("transfer_cant", "")

    return {
            "sender": sender,
            "addressee":addressee,
            "transfer_cant": transfer_cant
    }

def transfers_schema(accounts) -> list:
    return [transfer_schema(account) for account in accounts]