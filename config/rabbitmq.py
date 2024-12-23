import dotenv
import os
import pika

dotenv.load_dotenv()

if not os.environ.get("RABBIT_MQ_URL"):
    raise Exception("RABBIT_MQ_URL is not set")

parameters = pika.URLParameters(os.environ["RABBIT_MQ_URL"])

rabbitmq_connection = pika.BlockingConnection(parameters)
