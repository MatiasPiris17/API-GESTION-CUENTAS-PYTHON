from sanic import Sanic
from controllers.controller import transferController

def main() :
    app = Sanic("Transfers")

    app.add_route(transferController.as_view(), "/transfer")

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=8005, debug=True)
        # app.run(host='0.0.0.0', port=8005)

main()