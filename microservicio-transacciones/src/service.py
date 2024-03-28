from .database import transactions
from .transactions import Transactions

class TransactionService():

    async def getAuthenticatedAccounts(self, data: Transactions): # Se envia una peticion por remi y dist para verificar que existan
        return False # retorna un objeto con los datos del remitente y la cantidad de la transaccion 


    async def required_funds_check(self, data): # Se valida el que remi tenga los fondos necesarios para realizar la transaccion 
        return False


    async def createTransaction(self, data): # Se crea la transaccion en db
        transactions.append(data)
        return transactions
