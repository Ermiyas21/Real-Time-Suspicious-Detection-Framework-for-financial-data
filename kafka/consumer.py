from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'aml-topic',
    bootstrap_servers=['kafka:9092'],
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

def consume_messages():
    for message in consumer:
        print("hello worlds")
        print(message.value)
