from sanic.response import json
from sanic.views import HTTPMethodView
from sanic import exceptions
from .service import TransactionService
from .transactions import Transactions

class Transactions(HTTPMethodView):

    async def post(self, request):
        try:
            body = request.json

            if not body :
                raise exceptions.BadRequest("La solicitud no tiene cuerpo.")
            
            transaction = Transactions(**body)

            if not transaction.remitente or not transaction.destinatario or not transaction.transferencia:
                raise exceptions.BadRequest("Remitente, destinatario o transferencia faltante.")

            if not transaction.remitente.dni or not transaction.remitente.email:
                raise exceptions.BadRequest("Falta dni o email del remitente.")

            if not transaction.destinatario.dni or not transaction.destinatario.email:
                raise exceptions.BadRequest("Falta dni o email del destinatario.")
    
            methods = TransactionService()

            validateAccounts = await methods.getAuthenticatedAccounts(body) # valida que existan las cuentas en db
            if not validateAccounts : 
                raise exceptions.NotFound(f"Las cuentas no existen")
            check_founds = await methods.required_funds_check(validateAccounts) # valida que la cuenta tenga los fondos necesarios
            if not check_founds :
                raise exceptions.NotFound(f"El remitente no cuenta con los fondos necesarios para realizar la transaccion")
            new_transaction = await methods.createTransaction(body) # se crea la transaccion y se modifica la cantidad de las cuentas

            return json({"message": "Transaccion realizada con exito", "dates": new_transaction})
        
        except exceptions.BadRequest as e:
            return json({"error": str(e)}, status=400)
        
        except exceptions.NotFound as e:
            return json({"error": str(e)}, status=404)

        except Exception as e:
            print(e)
            return json({"error": "Error interno del servidor."}, status=500)
