from config.rabbitmq import rabbitmq_connection
from rabbitmq.queue import create_channel
from rabbitmq.consumer import register_consumer

from rabbitmq.tickets_queue import tickets_queue_callback

create_channel("tickets_queue", rabbitmq_connection)

register_consumer("tickets_queue", tickets_queue_callback)
