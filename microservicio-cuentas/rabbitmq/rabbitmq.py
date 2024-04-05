import pika
import json

class RabbitMQClient():

    def __init__(self):
        parameters = pika.ConnectionParameters(host='localhost')
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()

    async def consume_messages(self):
        
        def callback(ch, method, properties, body):
            print("Mensaje recibido: %r" % body)
            
            body = { 'response': True }
            self.channel.basic_publish(
                exchange='',
                routing_key='response_queue',
                body= json.dumps(body).encode()
            )

            print("Respuesta enviada:", json.dumps(body).encode())

        self.channel.queue_declare(queue='validation_queue')
        self.channel.basic_consume(queue='validation_queue', on_message_callback=callback, auto_ack=True)

        print('Escuchando la cola "validation_queue"')
        self.channel.start_consuming()
        
    
    async def close(self):
        self.channel.close()
        self.connection.close()