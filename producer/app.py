import pika
import json
import time


class PikaPublisher:
    def __init__(self, queue_name, exchange_name, exchange_type):
        self.credentials = pika.PlainCredentials('guest', 'guest')
        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672,
                                                                             credentials=self.credentials))
        self._channel = self._connection.channel()
        self._channel.exchange_declare(exchange=exchange_name, exchange_type=exchange_type)
        self.queue_name = queue_name

    def send_message(self, message_type, message):
        message = json.dumps({'type': message_type, 'message': message})
        self._channel.basic_publish(exchange='message_exchange', routing_key='message_queue', body=message)

    def close(self):
        self._connection.close()


if __name__ == '__main__':
    publisher = PikaPublisher(queue_name='message_queue',exchange_name='message_exchange', exchange_type='fanout')
    for i in range(3):
        time.sleep(5)
        publisher.send_message("a", "Hello World!")
        time.sleep(5)
        publisher.send_message("b", "Goodbye World!")
    publisher.close()