
from src.services.contracts.messaging_queue_contract import MessagingQueueContract


class RabbitMQMessagingTest(MessagingQueueContract):
    def send_to_queue(self):
        print('The message was sent')
