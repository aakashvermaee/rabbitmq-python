import pika

# connect to rabbitmq server on localhost
host = 'localhost'
connection = pika.BlockingConnection(pika.ConnectionParameters(host))
channel = connection.channel()

# declare/instantiate a queue
queue = 'hello'
channel.queue_declare(queue=queue)

# send message to queue = hello via exchange
message = 'hello, world!'
channel.basic_publish(exchange='', routing_key=queue, body=message)
print(" [x] Sent 'Hello World!'")

""" before porgram exists make sure metwork buffers were flushed and
message was actually delivered """
connection.close()
