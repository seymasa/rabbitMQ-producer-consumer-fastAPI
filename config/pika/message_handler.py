import json
from config.config import config
from common.utils.logger import logger


class MessageHandler:
    def __init__(self):
        self._handlers = {}

    def register_handler(self, message_type, handler):
        self._handlers[message_type] = handler

    async def handle_message(self, message):
        message_body = message.body
        try:
            message = json.loads(message_body.decode())
            logger.info(f' [✓] Received {message_body!r} on queue {config.RABBITMQ_QUEUE}')
            message_type = message.get("type")
            if message_type in self._handlers:
                logger.warning(f' [✓] message forwarded <successfully> to MQ Service for processing from MessageHandler..')
                await self._handlers[message_type](message)
                await message.ack()
        except json.decoder.JSONDecodeError:
            logger.error(f' [x] message forwarded <not successfully> to MQ Service for processing from MessageHandler..')
            await message.nack()
            logger.error(f' [x] Rejected {message_body!r} on queue {config.RABBITMQ_QUEUE}')
