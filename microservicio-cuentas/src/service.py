from .database import accounts # AccountsDb
from .account import Account

class AccountsService():
        
    async def getAccount(self, data): # Buscar una cuenta
        try:
            email = data.get("email")
            dni = data.get("dni")
            for account in accounts :
                emailAccount = account.get("email")
                dniAccount = account.get("dni")
                if(emailAccount == email or dniAccount == dni) :
                    return account
            return False
        except Exception as e:
            print(f"Error al obtener la cuenta: {e}")
            raise Exception
    

    async def postAccount(self, data): # Crear una cuenta si no existe, "money" se setea en 0
        email = data.get("email")
        dni = data.get("dni")
        for account in accounts :
            emailAccount = account.get("email")
            dniAccount = account.get("dni")
            if emailAccount == email or dniAccount == dni :
                return False
        data["money"] = 0
        accounts.append(data)
        return data
    
    
    async def putAccount(self, data): # Modificar una cuenta, buscando por dni o email
        email = data.get("email")
        dni = data.get("dni")
        for account in accounts: 
            emailAccount = account.get("email")
            dniAccount = account.get("dni")
            if emailAccount == email or dniAccount == dni :
                account.update(data)
                return accounts
        return False
    
    
    async def deleteAccount(self, data): # Elimiar una cuenta
        dni = data.get("dni")
        account_new =  [account for account in accounts if account.get("dni") != dni]
        if len(accounts) > len(account_new):
            return account_new
        else:
            return False