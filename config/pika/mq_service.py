from config.config import config
from config.pika.message_handler import MessageHandler
from config.pika.message_listener import PikaListener


@PikaListener(queue_name=config.RABBITMQ_QUEUE,
              exchange_name=config.RABBITMQ_EXCHANGE_NAME,
              exchange_type=config.RABBITMQ_EXCHANGE_TYPE)
class MQService:
    queue_name = config.RABBITMQ_QUEUE
    exchange_name = config.RABBITMQ_EXCHANGE_NAME
    exchange_type = config.RABBITMQ_EXCHANGE_TYPE

    def __init__(self):
        self.message_handler = MessageHandler()
        self.message_handler.register_handler("a_message", self.get_a_message)
        self.message_handler.register_handler("b_message", self.get_b_message)

    async def get_a_message(self, message):
        print(f"--> this message sanded from MQService: {message['message']}")

    async def get_b_message(self, message):
        print(f"--> this message sanded from MQService: {message['message']}")
