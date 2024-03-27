from sanic import Sanic, json
from src.controller import Accounts

app = Sanic("Accounts")

app.add_route(Accounts.as_view(), "/accounts")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
    # app.run(host='0.0.0.0', port=8000)