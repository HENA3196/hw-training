# Python implementation of the AMQP 0-9-1 protocol that tries to stay fairly independent of the underlying network support library. rabbitmq
# run :sudo service rabbitmq-server start
#     :sudo service rabbitmq-server stop
# in another terminal

import pika

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue
channel.queue_declare(queue='myqueue')

# Publish a message to the queue
x=channel.basic_publish(exchange='', routing_key='myqueue', body='Hello, World!')

# =============================================================

# Define the callback function to handle incoming messages
def callback(ch, method, properties, body):
    print("Received message: %r" % body)

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue
channel.queue_declare(queue='myqueue')

# Consume messages from the queue
channel.basic_consume(queue='myqueue', on_message_callback=callback, auto_ack=True)

# Start consuming
print("Waiting for messages. To exit press CTRL+C")
channel.start_consuming()

# Close the connection
connection.close()
