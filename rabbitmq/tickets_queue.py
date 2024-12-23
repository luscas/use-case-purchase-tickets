from config.db import session
from services.tickets_service import buy_ticket
import json


def tickets_queue_callback(ch, method, properties, body):
    payload = json.loads(body)
    user_id = payload["user_id"]
    ticket_id = payload["ticket_id"]

    buy_ticket(session, ticket_id, user_id)

    print(f"Received message: {body.decode()}")

    ch.basic_ack(delivery_tag=method.delivery_tag)
