from models.database import db_client
from models.transfer import transfer_schema, transfers_schema
from rabbitmq.rabbitmq import RabbitMQClient

class transferService(RabbitMQClient):
    async def getTransfers(self):
        transfers = db_client.transfers.find()
        return transfers_schema(transfers)

    async def createTransfer(self, data): 
        try: 
            await self.createQueue('validation_queue')
            await self.send('validation_queue', data)
            validation_response = await self.consume('response_queue', 'response_queue')
            print(validation_response)
            if not validation_response: 
                return False
            
            transfer_dict = dict(data)
            id = db_client.transfers.insert_one(transfer_dict).inserted_id
            new_transfer = transfer_schema(db_client.transfers.find_one({"_id": id}))

            return new_transfer
            # return {"test ": "test"}
        
        except Exception as e:
            return {"error": str(e)}
        

