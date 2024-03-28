from sanic import Sanic
from src.controller import transferController
# import pika

def main() :
    app = Sanic("Transfer")
    # connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    # channel = connection.channel()

    # channel.queue_declare(queue='hello')

    app.add_route(transferController.as_view(), "/transfer")

    if __name__ == "__main__":
        app.run(host="127.0.0.1", port=8081, debug=True)
        # app.run(host='0.0.0.0', port=8001)
    # connection.close()


main()