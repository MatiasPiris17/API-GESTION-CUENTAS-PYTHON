from sanic import Sanic
from controllers.controller import Accounts

def main():
    app = Sanic("Accounts")

    app.add_route(Accounts.as_view(), "/accounts")

    if __name__ == "__main__":
        app.run(host='0.0.0.0', port=8000, debug=True)
        # app.run(host='0.0.0.0', port=8000)

main()