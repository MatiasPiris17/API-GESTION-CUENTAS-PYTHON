from pydantic import BaseModel
from typing import Optional

# class Remitente():
#         dni:str
#         email:str
# class Destinatario():
#         dni:str
#         email:str

class Transfer(BaseModel):
    id: Optional[str]
    remitente: object
    destinatario: object
    trasferencia: str