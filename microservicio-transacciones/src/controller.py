from sanic.response import json
from sanic.views import HTTPMethodView
from sanic import exceptions
from .service import transferService

class transferController(HTTPMethodView):

    async def post(self, request):
        try:
            body = request.json

            if not body or ("remitente" not in body or "destinatario" not in body or "transfer" not in body):
                raise exceptions.BadRequest("Faltan datos en el cuerpo de la solicitud.")
            remitente = body["remitente"]
            if not remitente["dni"] or not remitente["email"]:
                raise exceptions.BadRequest("Falta dni o email del remitente.")
            destinatario = body["destinatario"]
            if not destinatario["dni"] or not destinatario["email"]:
                raise exceptions.BadRequest("Falta dni o email del destinatario.")
    
            methods = transferService()

            validateAccounts = await methods.getAuthenticatedAccounts(body) # valida que existan las cuentas en db
            if not validateAccounts : 
                raise exceptions.NotFound(f"Las cuentas no existen")
            #check_founds = await methods.required_funds_check(validateAccounts) # valida que la cuenta tenga los fondos necesarios
            #if not check_founds :
            #    raise exceptions.NotFound(f"El remitente no cuenta con los fondos necesarios para realizar la transaccion")
            new_transaction = await methods.createTransfer(body) # se crea la transaccion y se modifica la cantidad de las cuentas

            return json({"message": new_transaction})
        
        except exceptions.BadRequest as e:
            return json({"error": str(e)}, status=400)
        
        except exceptions.NotFound as e:
            return json({"error": str(e)}, status=404)

        except Exception as e:
            print(e)
            return json({"error": "Error interno del servidor."}, status=500)
