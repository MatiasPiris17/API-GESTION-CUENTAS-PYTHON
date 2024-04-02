from models.database import db_client # , transfer_schema
# from .transfer import Transfer
from models.transfer import transfer_schema, transfers_schema, Transfer

class transferService():
    async def getTransfers(self):
        transfers = db_client.transfers.find()
        return transfers_schema(transfers)
        # return Transfer(**transfers_schema(transfers))

    async def createTransfer(self, data): 
        try: 
            transfer_dict = dict(data)
            id = db_client.transfers.insert_one(transfer_dict).inserted_id
            new_transfer = transfer_schema(db_client.transfers.find_one({"_id": id}))
            return new_transfer
        
        except Exception as e:
            return {"error": str(e)}
        

    # async def getAuthenticatedAccounts(self, data): 
    #     return True

    # async def required_funds_check(self, data): 
    #     try: 
    #         remitente = data.get("remitente")
    #         money = int(remitente.get("money"))
    #         transfer = int(data.get("transfer"))

    #         if money < transfer :
    #             return False
    #         return {"success": "La cuenta tiene los fondos necesarios"}
    #     except Exception as e:
    #         return {"error": str(e)}


