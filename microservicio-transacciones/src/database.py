transactions = [
    { 
        "remitente": {
            "dni": "43859605",
            "email": "matiaslinkedin17@gmail.com"
        },
        "destinatario": {
            "dni": "43859605",
            "email": "matiaslinkedin17@gmail.com"
        },
        "trasferencia": 600
    }, 
    {         
        "remitente": {
            "dni": "89648564",
            "email": "matiaslink@gmail.com"
        },
        "destinatario": {
            "dni": "12345678",
            "email": "mastv@gmail.com"
        },
        "trasferencia": 540
    },
    { 
        "remitente": {
            "dni": "43859605",
            "email": "matiaslinkedin17@gmail.com"
        },
        "destinatario": {
            "dni": "43859605",
            "email": "matiaslinkedin17@gmail.com"
        },
        "trasferencia": 40
    },
    { 
        "remitente": {
            "dni": "43859605",
            "email": "matiaslinkedin17@gmail.com"
        },
        "destinatario": {
            "dni": "43859605",
            "email": "matiaslinkedin17@gmail.com"
        },
        "trasferencia": 50
    }
]

from pymongo import MongoClient

# db_client = MongoClient("mongodb+srv://root:root@cluster0.w5vafrc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0").local
db_client = MongoClient("mongodb+srv://root:root@cluster0.w5vafrc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0").challenge

def transfer_schema(transaction): 
    remitente = transaction["remitente"]
    destinatario = transaction["destinatario"]
    print(transaction)
    return {
            "id": str(transaction["_id"]),
            "remitente": { "dni":  remitente.get("dni", ""), "email": remitente.get("email", "")},
            "destinatario": { "dni":  destinatario.get("dni", ""), "email": destinatario.get("email", "")},
            "transfer": transaction.get("transfer")
    }

def transfers_schema(accounts) -> list:
    return [transfer_schema(account) for account in accounts]