from sanic import Sanic
# import pika
from src.controller import Transactions

def main() :
    app = Sanic("Transactions")
    # connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    # channel = connection.channel()

    # channel.queue_declare(queue='hello')

    app.add_route(Transactions.as_view(), "/transactions")

    if __name__ == "__main__":
        app.run(host="127.0.0.1", port=8081, debug=True)
        # app.run(host='0.0.0.0', port=8001)
    # connection.close()


main()