from .database import db_client # , transfer_schema, transactions
# from .transfer import Transfer

class transferService():

    async def getAuthenticatedAccounts(self, data): 
        return True


    async def required_funds_check(self, data): 
        #ej data: { remitente: { dni, mail, money }, transfer }
        try: 
            remitente = data.get("remitente")
            money = int(remitente.get("money"))
            transfer = int(data.get("transfer"))

            if money < transfer :
                return False
            return {"success": "La cuenta tiene los fondos necesarios"}
        except Exception as e:
            return {"error": str(e)}


    async def createTransfer(self, data): # Agregar peticion PUT para moficar la cantidad de cada cuenta
        try: 
            #id = db_client.transfer.insert_one(transfer_dic).inserted_id
            #new_transaction = transfer_schema(db_client.transfer.find_one({"_id": id}))
            transfer_dic = dict(data)
            db_client.transfer.insert_one(transfer_dic)
            return {"success": "Trasferencia enviada"}
        except Exception as e:
            return {"error": str(e)}