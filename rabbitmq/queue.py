import json
from config.rabbitmq import rabbitmq_connection


def create_channel(queue_name, connection):
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)
    return channel


def call_channel(queue_name, payload, session):
    connection = rabbitmq_connection
    channel = create_channel(queue_name, connection)
    channel.basic_publish(
        exchange="",
        routing_key=queue_name,
        body=json.dumps(payload),
    )
    channel.close()
    connection.close()
    session.close()
