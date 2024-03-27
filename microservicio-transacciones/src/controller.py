from sanic.response import json
from sanic.views import HTTPMethodView
from sanic import exceptions
from .service import TransactionService

class Transactions(HTTPMethodView):

    async def get(self, request): 
        try:
            body = request.json

            if not body :
                raise exceptions.BadRequest("La solicitud no tiene cuerpo.")
            if "dni" not in body :
                raise exceptions.BadRequest("DNI faltante.")
            if "email" not in body : 
                raise exceptions.BadRequest("Email faltante.")


            methods = TransactionService()
            accounts = await methods.getTransaction(body)

            if not accounts:
                raise exceptions.NotFound(f"No se encontró ningún transacciones con email: {body['email']} y dni: {body['dni']}")

            return json(accounts)
        
        except exceptions.BadRequest as e:
            return json({"error": str(e)}, status=400)

        except exceptions.NotFound as e:
            return json({"error": str(e)}, status=404)

        except Exception as e:
            print(e)
            return json({"error": "Error interno del servidor."}, status=500)
    

    async def post(self, request):
        try:
            body = request.json

            if not body :
                raise exceptions.BadRequest("La solicitud no tiene cuerpo.")
            if "remitente" not in body or "destinatario" not in body or "transferencia" not in body: 
                raise exceptions.BadRequest("Remitente, destinatario o transferencia faltante.")
            if "dni" not in body["remitente"] or "dni" not in body["destinatario"] : 
                raise exceptions.BadRequest("Falta dni de las cuentas.")
            if "email" not in body["remitente"] or "email" not in body["destinatario"] : 
                raise exceptions.BadRequest("Falta email de las cuentas.")

            methods = TransactionService()
            accounts = await methods.postTransaction(body)

            return json(accounts)
        
        except exceptions.BadRequest as e:
            return json({"error": str(e)}, status=400)

        except Exception as e:
            return json({"error": "Error interno del servidor."}, status=500)
