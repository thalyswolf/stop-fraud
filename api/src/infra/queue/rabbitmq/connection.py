import pika
class RabbitConnection:

    _connection = None


    def __init__(self):
        if self._connection is None:
            self._connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    
    def send_message(self, data: str):
        channel = self._connection.channel()
        channel.queue_declare(queue='messages')

        channel.basic_publish(exchange='', routing_key='hello', body=data)
