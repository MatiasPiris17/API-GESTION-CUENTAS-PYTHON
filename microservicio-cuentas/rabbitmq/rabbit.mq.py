import pika
import json

class RabbitMQClient():

    def __init__(self):
        parameters = pika.ConnectionParameters(host='localhost')
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()

    async def createQueue(self, queue_name):
        self.channel.queue_declare(queue= queue_name)
        
    async def send(self, queue_name, body):
        self.channel.queue_declare(queue=queue_name)

        self.channel.basic_publish(
            exchange= '',
            routing_key=queue_name,
            body=json.dumps(body).encode()
        )
        print(f"Message sent: {body}")
    
    async def consume(self, queue_name):
        self.channel.queue_declare(queue='response_queue')
        method_frame, header_frame, body  = self.channel.basic_get('response_queue')

        if method_frame:
            self.channel.basic_ack(method_frame.delivery_tag)
            print('Response received: ', body)
            return method_frame, header_frame, body
        else:
            print('No response received.')
        
    
    async def close(self):
        self.channel.close()
        self.connection.close()