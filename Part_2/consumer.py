import pika
import json
from models import Contact
from connection import mongo_connect

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='email_queue')


def send_email_dummy(email):
    print(f"Sending email to {email}")


def consume_messages():
    def callback(ch, method, properties, body):
        message = json.loads(body)
        contact_id = message.get('contact_id')
        if contact_id:
            contact = Contact.objects(id=contact_id).first()
            if contact and not contact.is_message_sent:
                send_email_dummy(contact.email)
                contact.is_message_sent = True
                contact.save()
                print(f"Email sent to {contact.email}")

    channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)

    print('Waiting for messages')
    channel.start_consuming()


if __name__ == "__main__":
    mongo_connect()
    consume_messages()
