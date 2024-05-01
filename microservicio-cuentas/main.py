from sanic import Sanic
from controllers.controller import Accounts
from rabbitmq.rabbitmq import RabbitMQClient
import threading

async def main():
    app = Sanic("Accounts")

    events_consumer = RabbitMQClient()
    events_consumer = await events_consumer.consume_messages()
    # @app.listener('before_server_start')
    # async def setup_connection(app, loop):
    #     await events_consumer.consume_messages()

    # @app.listener('after_server_stop')
    # async def close_connection(app, loop):
    #     await events_consumer.close()

    app.add_route(Accounts.as_view(), "/accounts")

    if __name__ == "__main__":
        # Iniciar el hilo para consumir mensajes de RabbitMQ
        rabbitmq_thread = threading.Thread(target=events_consumer)
        rabbitmq_thread.start()

        app.run(host='0.0.0.0', port=8000, debug=True)
        # app.run(host='0.0.0.0', port=8000)


main()