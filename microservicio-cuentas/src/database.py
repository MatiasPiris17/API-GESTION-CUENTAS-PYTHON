accounts = [
    { "name": "Matias", "email": "matiaslinkedin17@gmail.com", "dni": "43859605",  "money": 500.2 }, 
    { "name": "Marco", "email": "marcos125@gmail.com", "dni": "45698564",  "money": 200 },
    { "name": "Camila", "email": "camilads@gmail.com", "dni": "23648975",  "money": 150 },
    { "name": "Pablo", "email": "pmamani@gmail.com", "dni": "43864521",  "money": 550 }
    ]

# url mongo local dev: mongodb+srv://root:root@cluster0.w5vafrc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
# ulr mongo compose: mongodb://root:root@localhost:27017/?authSource=admin

from pymongo import MongoClient

# db_client = MongoClient("mongodb+srv://root:root@cluster0.w5vafrc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0").local
db_client = MongoClient("mongodb+srv://root:root@cluster0.w5vafrc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0").challenge

def account_schema(account) -> dict: 
    name = account.get("name", "")
    money = account.get("money", 0)

    return {
            "id": str(account["_id"]),
            "name": name,
            "email": account["email"],
            "dni": account["dni"],
            "money": money
            }


def accounts_schema(accounts) -> list:
    return [account_schema(account) for account in accounts]