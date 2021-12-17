
from src.services.contracts.messaging_queue_contract import MessagingQueueContract
from src.infra.queue.rabbitmq.connection import RabbitConnection

class RabbitMQMessaging(MessagingQueueContract):
    def send_to_queue(self):
        RabbitConnection().send_message('null')
        print('The message was sent')
