from sanic import Sanic
from sanic_motor import BaseModel
from src.controller import Accounts
from src.database import settings

app = Sanic("Accounts")

app.config.update(settings)

BaseModel.init_app(app)

app.add_route(Accounts.as_view(), "/accounts")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
    # app.run(host='0.0.0.0', port=8000)