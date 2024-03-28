from .database import db_client, account_schema, accounts_schema # AccountsDb

class AccountsService():
    async def getAccount(self, data):
        dni = data.get("dni")
        try:
            search = db_client.accounts.find_one({"dni": dni})

            if not search :
                return False
            account = account_schema(search)
            return account
            
        except Exception as e:
            return {"error": str(e)}
    

    async def postAccount(self, data): 
        dni = data.get("dni")
        try:
            account_dup = db_client.accounts.find_one({"dni": dni})
            if account_dup :
                return False
            account_dic = dict(data)
            id = db_client.accounts.insert_one(account_dic).inserted_id
            new_account = account_schema(db_client.accounts.find_one({"_id": id}))
            return new_account
        except Exception as e:
            return {"error": str(e)}
    
    
    async def putAccount(self, data): 
        dni = data.get("dni")
        try: 
            updated_account = db_client.accounts.find_one_and_replace({"dni": dni}, data)
            if not updated_account:
                return False
            account = account_schema(db_client.accounts.find_one({"dni": dni}))
            return account
        except Exception as e:
            return {"error": str(e)}
    

    async def deleteAccount(self, data): # Elimiar una cuenta
        dni = data.get("dni")
        try:
            account = db_client.accounts.find_one({"dni": dni})
            if not account:
                return False
            db_client.accounts.delete_one({"dni": dni})
            return {"success": "Cuenta eliminada correctamente"}
        except Exception as e:
            return {"error": str(e)}