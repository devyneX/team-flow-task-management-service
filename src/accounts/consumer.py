import json
import threading

import pika

from src.accounts.serializers import UserSerializer

ROUTING_KEY = 'user.created.key'
EXCHANGE = 'user_exchange'
THREADS = 5


class UserCreatedConsumer(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = connection.channel()
        self.channel.exchange_declare(exchange=EXCHANGE, exchange_type='direct')
        # self.channel.queue_declare(queue=QUEUE_NAME, auto_delete=False)
        result = self.channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue
        self.channel.queue_bind(queue=queue_name, exchange=EXCHANGE, routing_key=ROUTING_KEY)
        self.channel.basic_qos(prefetch_count=THREADS * 10)
        self.channel.basic_consume(queue=queue_name, on_message_callback=self.callback)

    def callback(self, channel, method, properties, body):
        if properties.content_type != 'user_created_method':
            return

        message = json.loads(body)
        print(message)
        print(type(message))
        channel.basic_ack(delivery_tag=method.delivery_tag)
        serializer = UserSerializer(data=message)
        print(serializer.initial_data)
        if serializer.is_valid():
            serializer.save()
            print('User created:  ', serializer.instance)
        else:
            print(serializer.errors)

    def run(self):
        print('Inside TM Service:  Created Listener ')
        self.channel.start_consuming()
