from connection import mongo_connect
from models import Contact
from faker import Faker
import pika
import json


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='email_queue')

def fake_data():
    fake = Faker()
    for _ in range(20):
        full_name = fake.name()
        email = fake.email()
        yield {"full_name": full_name, "email": email}

def publish_messages():
    for contact_data in fake_data():
        contact = Contact(**contact_data)
        contact.save()

        # RabbitMQ publication
        message = {"contact_id": str(contact.id)}
        body = json.dumps(message).encode('utf-8')
        channel.basic_publish(exchange='', routing_key='email_queue', body=body)

    print("Messages published to the queue")
    connection.close()

if __name__ == "__main__":
    mongo_connect()
    publish_messages()


