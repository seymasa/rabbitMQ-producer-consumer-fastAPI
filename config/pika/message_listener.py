import asyncio
import aio_pika
from common.utils.logger import logger
from config.config import config
from config.pika.message_handler import MessageHandler


class PikaListener:
    def __init__(self, queue_name, exchange_name, exchange_type):
        self.queue_name = queue_name
        self.exchange_name = exchange_name
        self.exchange_type = exchange_type

    def __call__(self, cls):
        async def __init__(self, *args, **kwargs):
            super(cls, self).__init__(*args, **kwargs)
            self._connection = await aio_pika.connect(
                host=config.RABBITMQ_HOST,
                port=config.RABBITMQ_PORT,
                login=config.RABBITMQ_USERNAME,
                password=config.RABBITMQ_PASSWORD)
            self._channel = await self._connection.channel()
            logger.info(f'Connected pika consumer to {config.RABBITMQ_HOST}')
            await self._channel.declare_exchange(self.exchange_name, self.exchange_type)
            await self._channel.declare_queue(self.queue_name)
            await self.queue.bind(queue=self.queue_name,exchange=self.exchange_name)
            await self.queue.consume(self.queue_name, self.message_handler.handle_message)
            logger.info(' [*] Waiting for messages on queue.')

        async def listen(self):
            try:
                while True:
                    await asyncio.sleep(0.1)
                    self._channel.start_consuming()
            except KeyboardInterrupt as e:
                logger.exception(e)
            except Exception as e:
                logger.exception(e)

        async def stop(self):
            await self._channel.cancel()
            await self._connection.close()

        def __del__(self):
            self.stop()

        cls.message_handler = MessageHandler()
        cls.__init__ = __init__
        cls.listen = listen
        cls.stop = stop
        return cls
