from .database import accounts

class AccountsService():

    async def getAccounts(self):
        data = accounts
        return data
    
    async def getAccount(self, data):
        for account in accounts:
            if account["email"] == data["email"] or account["dni"] == data["dni"] :
                return account
        return False
    
    async def postAccount(self, data):
        accounts.append(data)
        return accounts
    
    async def putAccount(self, data):
        for account in accounts: 
            if account["email"] == data["email"] or account["dni"] == data["dni"] :
                account.update(data)
                return accounts
        return False
    
    async def deleteAccount(self, data):
        dni = data["dni"]
        email = data["email"]
        dates = []
        for account in accounts : 
            if ( (account["email"] != email) or (account["dni"] != dni) ):
                dates.append(account)
        return dates