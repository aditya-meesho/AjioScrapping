from kafka import KafkaProducer
from json import dumps
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)


def ProduceEvent(data, Topic):
    try:
        producer.send(Topic, value=data)
        producer.flush()
    except Exception as e:
        logger.error(f"KafkaProducer.ProduceEvent , Error producing message: {e}")

