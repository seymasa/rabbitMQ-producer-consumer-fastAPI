import json
from config.config import config
from common.utils.logger import logger


class MessageHandler:
    def __init__(self):
        self._handlers = {}

    def register_handler(self, message_type, handler):
        self._handlers[message_type] = handler

    def handle_message(self, channel, method, properties, body):

        try:
            message = json.loads(body.decode())
            channel.basic_nack(delivery_tag=method.delivery_tag, requeue=False)
            logger.info(f' [✓] Received {body!r} on queue {config.RABBITMQ_QUEUE}')
            message_type = message.get("type")
            if message_type in self._handlers:
                logger.warning(f' [✓] message forwarded <successfully> to MQ Service for processing from MessageHandler..')
                self._handlers[message_type](message)
        except json.decoder.JSONDecodeError:
            logger.error(f' [x] message forwarded <not successfully> to MQ Service for processing from MessageHandler..')
            channel.basic_nack(delivery_tag=method.delivery_tag, requeue=False)
            logger.error(f' [x] Rejected {body!r} on queue {config.RABBITMQ_QUEUE}')
