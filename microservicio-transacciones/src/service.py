from .database import transactions

class TransactionService():

    async def getTransaction(self, data):
        transaction_account = []
        for transaction in transactions:
            if (transaction["remitente"]["dni"] == data["dni"]) or (transaction["remitente"]["email"] == data["email"]) :
                transaction_account.append(transaction)
            
        return len(transaction_account) < 0 if False else transaction_account

    async def postTransaction(self, data):
        transactions.append(data)
        return transactions
