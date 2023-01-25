from config.config import config
from config.pika.message_listener import PikaListener


@PikaListener(queue_name=config.RABBITMQ_QUEUE,
              exchange_name=config.RABBITMQ_EXCHANGE_NAME,
              exchange_type=config.RABBITMQ_EXCHANGE_TYPE)
class MQService(object):
    queue_name = config.RABBITMQ_QUEUE
    exchange_name = config.RABBITMQ_EXCHANGE_NAME
    exchange_type = config.RABBITMQ_EXCHANGE_TYPE

    def __init__(self):
        super().__init__()

    @staticmethod
    def get_a_message(message):
        print(f"--> this message sanded from MQService: {message['message']}")

    @staticmethod
    def get_b_message(message):
        print(f"--> this message sanded from MQService: {message['message']}")
