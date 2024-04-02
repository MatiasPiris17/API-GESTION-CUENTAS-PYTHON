from sanic.response import json
from sanic.views import HTTPMethodView
from sanic import exceptions
from services.service import AccountsService

class Accounts(HTTPMethodView):

    async def get(self, request): 
        try:
            body = request.json

            if not body or ("email" not in body):
                raise exceptions.BadRequest("Missing data in request body.")
            
            methods = AccountsService()
            account = await methods.getAccount(body)
            if not account : 
                raise exceptions.NotFound(f"Account not found")
            
            return json({"success": account})
        
        except exceptions.BadRequest as e:
            return json({"error": str(e)}, status=400)

        except exceptions.NotFound as e:
            return json({"error": str(e)}, status=404)

        except Exception as e:
            print(e)
            return json({"error": "Internal Server Error."}, status=500)
    

    async def post(self, request):
        try:

            body = request.json

            if not body or ("dni" not in body or "email" not in body or "name" not in body):
                raise exceptions.BadRequest("Missing data in request body.")

            methods = AccountsService()
            account = await methods.postAccount(body)
            if not account:
                raise exceptions.NotFound(f"Account already exists")

            return json({"success": account})
        
        except exceptions.BadRequest as e:
            return json({"error": str(e)}, status=400)
        
        except exceptions.NotFound as e:
            return json({"error": str(e)}, status=404)

        except Exception as e:
            print(e)
            return json({"error": "Internal Server Error"}, status=500)
    

    async def put(self, request):
        try:
            body = request.json

            if not body or ("email" not in body):
                raise exceptions.BadRequest("Missing data in request body.")

            methods = AccountsService()
            accounts = await methods.putAccount(body)

            if not accounts:
                raise exceptions.NotFound(f"Account not found.")

            return json({"success": accounts})
        
        except exceptions.BadRequest as e:
            return json({"error": str(e)}, status=400)
        
        except exceptions.NotFound as e:
            return json({"error": str(e)}, status=404)

        except Exception as e:
            print(e)
            return json({"error": "Internal Server Error."}, status=500)
    
    
    async def delete(self, request):
        try:
            body = request.json

            if not body or ("email" not in body):
                raise exceptions.BadRequest("Missing data in request body.")

            methods = AccountsService()
            accounts = await methods.deleteAccount(body)
            if not accounts :
                raise exceptions.NotFound(f"Account not found.")

            return json({"success": "Successfully deleted account"})

        except exceptions.BadRequest as e:
            return json({"error": str(e)}, status=400)
        
        except exceptions.NotFound as e:
            return json({"error": str(e)}, status=404)

        except Exception as e:
            print(e)
            return json({"error": "Internal Server Error."}, status=500)