from src.infra.queue.rabbitmq.rabbitmq import RabbitMQMessaging

def get_messaging_queue_factory():
    return RabbitMQMessaging()
