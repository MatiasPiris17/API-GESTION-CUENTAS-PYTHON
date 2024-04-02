from models.database import db_client
from models.account import account_schema, accounts_schema

class AccountsService():
    async def getAccount(self, data):
        try:
            search_account = db_client.accounts.find_one({"email": data["email"]})

            if not search_account :
                return False
            
            return account_schema(search_account)
            
        except Exception as e:
            return {"error": str(e)}
    

    async def postAccount(self, data): 
        try:
            account_dict = dict(data)
            account_dict["money"] = 0

            id = db_client.accounts.insert_one(account_dict).inserted_id
            new_account = account_schema(db_client.accounts.find_one({"_id": id}))

            return new_account
        except Exception as e:
            return {"error": str(e)}
    
    
    async def putAccount(self, data): 
        try: 
            search_account = db_client.accounts.find_one({"email": data["email"]})
            if not search_account :
                return False
            
            db_client.accounts.update_one({"email": data["email"]}, {"$set": data})

        except:
            return {"error": "Account has not been updated"}
        
        account = account_schema(db_client.accounts.find_one({"email": data["email"]}))
        return account
        

    async def deleteAccount(self, data): 
        try:
            account = db_client.accounts.find_one({"email": data["email"]})
            if not account:
                return False
            
            db_client.accounts.delete_one({"email": data["email"]})

            return {"success": "Successfully deleted account"}
        
        except Exception as e:
            return {"error": str(e)}

        