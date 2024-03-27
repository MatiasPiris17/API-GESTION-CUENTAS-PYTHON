from .database import accounts
from database import Accounts

class AccountsService():

    async def getAccounts(self):
        data = accounts
        return data
        
    async def getAccount(self, data):
        try:
            # for account in accounts:
            #     if account["email"] == data["email"] or account["dni"] == data["dni"] :
            #         return account

            email = data["email"]
            dni = data["dni"]

            account = await Accounts.find_one({ "email": email, "dni": dni })

            if not account or len(account) == 0 : 
                return False
            return account

        except Exception as e:
            print(f"Error al obtener la cuenta: {e}")
            raise Exception
    
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