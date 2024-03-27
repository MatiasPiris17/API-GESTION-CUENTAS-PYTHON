
# accounts = [
#     { "name": "Matias", "email": "matiaslinkedin17@gmail.com", "dni": "43859605",  "money": 500.2 }, 
#     { "name": "Marco", "email": "marcos125@gmail.com", "dni": "45698564",  "money": 200 },
#     { "name": "Camila", "email": "camilads@gmail.com", "dni": "23648975",  "money": 150 },
#     { "name": "Pablo", "email": "pmamani@gmail.com", "dni": "43864521",  "money": 550 }
#     ]

# ulr mongo: mongodb://root:root@localhost:27017/?authSource=admin
from sanic_motor import BaseModel

settings = dict(
    MOTOR_URI= "mongodb://root:root@localhost:27017/?authSource=admin",
    LOGO=None,
)

class Accounts(BaseModel):
    __coll__ = "accounts"
