from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    data = {
        "temperature": random.randint(20, 35),
        "humidity": random.randint(40, 80)
    }

    producer.send("weather", data)
    print("Sent:", data)
    time.sleep(2)
