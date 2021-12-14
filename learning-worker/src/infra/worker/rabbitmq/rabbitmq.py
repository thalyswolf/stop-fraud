from traceback import format_exc

from src.core.controller.to_learning_controller import ToLearningController
from src.infra.worker.rabbitmq.connection import RabbitConnection


def send_to_controller(ch, method, properties, body):
    print('received message')
    ToLearningController().to_learning()

def on_listening():
    try:
        RabbitConnection().listening_messages(send_to_controller)
    except:
        print(format_exc())
        on_listening()

on_listening()