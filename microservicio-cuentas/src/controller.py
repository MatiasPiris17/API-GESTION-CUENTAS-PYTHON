from sanic.response import json
from sanic.views import HTTPMethodView
from sanic import exceptions
from .service import AccountsService

class Accounts(HTTPMethodView):

    async def get(self, request): 
        try:
            body = request.json

            if not body or ("dni" not in body or "email" not in body):
                raise exceptions.BadRequest("Faltan datos en el cuerpo de la solicitud.")

            methods = AccountsService()
            accounts = await methods.getAccount(body)

            if not accounts:
                raise exceptions.NotFound(f"No se encontró ningún usuario con email: {body['email']} y dni: {body['dni']}")

            return json(accounts)
        
        except exceptions.BadRequest as e:
            return json({"error": str(e)}, status=400)

        except exceptions.NotFound as e:
            return json({"error": str(e)}, status=404)

        except Exception as e:
            return json({"error": "Error interno del servidor."}, status=500)
    

    async def post(self, request):
        try:
            body = request.json

            if not body or ("dni" not in body or "email" not in body):
                raise exceptions.BadRequest("Faltan datos en el cuerpo de la solicitud.")

            methods = AccountsService()
            accounts = await methods.postAccount(body)

            return json(accounts)
        
        except exceptions.BadRequest as e:
            return json({"error": str(e)}, status=400)

        except Exception as e:
            return json({"error": "Error interno del servidor."}, status=500)
    

    async def put(self, request):
        try:
            body = request.json

            if not body or ("dni" not in body or "email" not in body):
                raise exceptions.BadRequest("Faltan datos en el cuerpo de la solicitud.")

            methods = AccountsService()
            accounts = await methods.putAccount(body)

            if not accounts:
                raise exceptions.NotFound(f"No se encontró ningún usuario con email: {body['email']} y dni: {body['dni']}")

            return json(accounts)
        
        except exceptions.BadRequest as e:
            return json({"error": str(e)}, status=400)
        
        except exceptions.NotFound as e:
            return json({"error": str(e)}, status=404)

        except Exception as e:
            return json({"error": "Error interno del servidor."}, status=500)
    
    
    async def delete(self, request):
        try:
            body = request.json

            if not body or ("dni" not in body or "email" not in body):
                raise exceptions.BadRequest("Faltan datos en el cuerpo de la solicitud.")

            methods = AccountsService()
            accounts = await methods.deleteAccount(body)

            return json(accounts)

        except exceptions.BadRequest as e:
            return json({"error": str(e)}, status=400)
        
        except exceptions.NotFound as e:
            return json({"error": str(e)}, status=404)

        except Exception as e:
            return json({"error": "Error interno del servidor."}, status=500)