from config.db import session
from rabbitmq.queue import call_channel

payload = {"user_id": 1, "ticket_id": 1}

call_channel("tickets_queue", payload, session)
