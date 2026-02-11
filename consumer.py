from kafka import KafkaConsumer
import psycopg2
import json

consumer = KafkaConsumer(
    "weather",
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

conn = psycopg2.connect(
    dbname="pipeline_db",
    user="user",
    password="password",
    host="localhost"
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS weather (
    temperature INT,
    humidity INT
)
""")
conn.commit()

for message in consumer:
    data = message.value

    cur.execute(
        "INSERT INTO weather (temperature, humidity) VALUES (%s, %s)",
        (data["temperature"], data["humidity"])
    )
    conn.commit()

    print("Inserted:", data)
