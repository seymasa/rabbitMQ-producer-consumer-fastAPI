import pika
from common.utils.logger import logger
from config.config import config
from config.pika.message_handler import MessageHandler


class PikaListener:
    def __init__(self, queue_name, exchange_name, exchange_type):
        self.queue_name = queue_name
        self.exchange_name = exchange_name
        self.exchange_type = exchange_type

    def __call__(self, cls):
        def __init__(self, *args, **kwargs):
            super(cls, self).__init__(*args, **kwargs)

            self.credentials = pika.PlainCredentials(config.RABBITMQ_USERNAME, config.RABBITMQ_PASSWORD)
            self._connection = pika.BlockingConnection(pika.ConnectionParameters(host=config.RABBITMQ_HOST,
                                                                                 port=config.RABBITMQ_PORT,
                                                                                 credentials=self.credentials))
            self._channel = self._connection.channel()
            logger.info(f'Connected pika consumer to {config.RABBITMQ_HOST}')
            self._channel.exchange_declare(exchange=self.exchange_name, exchange_type=self.exchange_type)
            self._channel.queue_declare(queue=self.queue_name)
            self._channel.queue_bind(queue=self.queue_name, exchange=self.exchange_name, routing_key='')
            self._channel.basic_consume(queue=self.queue_name,
                                        on_message_callback=self.message_handler.handle_message,
                                        auto_ack=False)
            logger.info(' [*] Waiting for messages on queue.')

        def listen(self):
            try:
                self._channel.start_consuming()
            except KeyboardInterrupt as e:
                logger.exception(e)
            except Exception as e:
                logger.exception(e)

        def stop(self):
            self._channel.stop_consuming()
            self._connection.close()

        def __del__(self):
            self.stop()

        cls.message_handler = MessageHandler()
        cls.__init__ = __init__
        cls.listen = listen
        cls.stop = stop
        return cls
