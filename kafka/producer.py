from confluent_kafka import admin, Producer
import pickle

KAFKA_CONFIG = {
    "bootstrap.servers": "localhost:9092"
}

kafka_client = admin.AdminClient(KAFKA_CONFIG)
new_topic = admin.NewTopic("test", 1, 1)
kafka_client.create_topics([new_topic])
producer = Producer(KAFKA_CONFIG)
print(kafka_client)

while True:
    a = input("ingrese mensaje: ")
    producer.produce("test", pickle.dumps(a))




