from confluent_kafka import Consumer
import pickle

CONSUMER_CONFIG = {
    'bootstrap.servers': '0.0.0.0:9092',
    'group.id': 'test',
    'auto.offset.reset': 'earliest',
}


consumer = Consumer(CONSUMER_CONFIG)
consumer.subscribe(['test'])
print(consumer)
while True:
    msg = consumer.poll(2)
    if msg:
        data = pickle.loads(msg.value())
        print(data)


