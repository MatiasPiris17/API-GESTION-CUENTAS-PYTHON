from sanic import Sanic
from src.controller import Transactions

app = Sanic("Transactions")
    
app.add_route(Transactions.as_view(), "/transactions")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8081, debug=True)