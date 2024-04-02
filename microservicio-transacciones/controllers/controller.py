from sanic.response import json
from sanic.views import HTTPMethodView
from sanic import exceptions
from services.service import transferService

class transferController(HTTPMethodView):
    async def get(self, request):
        try:
            methods = transferService()
            validateAccounts = await methods.getTransfers()
            return json(validateAccounts)
        except Exception as e:
            print(e)
            return json({"error": "Internal Server Error."}, status=500)

    async def post(self, request):
        try:
            body = request.json

            if not body or ("sender" not in body or "addressee" not in body or "transfer_cant" not in body):
                raise exceptions.BadRequest("Missing data in request body.")
    
            methods = transferService()
            new_transfer = await methods.createTransfer(body) 

            return json({"success": new_transfer})
        
        except exceptions.BadRequest as e:
            return json({"error": str(e)}, status=400)
        
        except exceptions.NotFound as e:
            return json({"error": str(e)}, status=404)

        except Exception as e:
            print(e)
            return json({"error": "Internal Server Error."}, status=500)
