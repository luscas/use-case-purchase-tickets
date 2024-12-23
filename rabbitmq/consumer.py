from config.rabbitmq import rabbitmq_connection

channel = rabbitmq_connection.channel()


def register_consumer(queue_name, callback):
    channel.queue_declare(queue=queue_name)
    channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=False
    )
    channel.basic_qos(prefetch_count=1)
    print(f"Waiting for messages in queue '{queue_name}'. Press Ctrl+C to exit.")
    channel.start_consuming()
