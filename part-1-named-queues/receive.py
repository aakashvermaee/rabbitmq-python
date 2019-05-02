import pika

# connect to rabbitmq server on localhost
host = 'localhost'
connection = pika.BlockingConnection(pika.ConnectionParameters(host))
channel = connection.channel()

# make sure that the queue exists
queue = 'hello'
channel.queue_declare(queue=queue)

""" run callback function whenever a new message arrives
in the queue """

def callback(ch, method, properties, body):
    print("[x] Received %r" % body)


# Pass callback reference to rabbitmq
channel.basic_consume(queue=queue, auto_ack=True, on_message_callback=callback)

""" keep program in an infinite loop to receive messages
whenever produced by the sender """

print("[*] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()