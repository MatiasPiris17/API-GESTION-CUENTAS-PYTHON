from sanic import Sanic
from src.controller import Accounts

app = Sanic("accounts")
    
app.add_route(Accounts.as_view(), "/accounts")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)