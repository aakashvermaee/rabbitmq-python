import sys
import pika

# connect to rabbitmq server on localhost
host = 'localhost'
connection = pika.BlockingConnection(pika.ConnectionParameters(host))
channel = connection.channel()

# declare/instantiate a queue
queue = 'task_queue_2'
channel.queue_declare(queue=queue, durable=True)

# send message to queue = hello via exchange
message = ' '.join(sys.argv[1:]) or "Hello World"
channel.basic_publish(exchange='', routing_key=queue, body=message)
print(" [x] Sent %r" % message)

""" before porgram exists make sure metwork buffers were flushed and
message was actually delivered """
connection.close()
