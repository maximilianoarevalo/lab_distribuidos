from confluent_kafka import Consumer
import pickle


CONSUMER_CONFIG = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'test',
    'auto.offset.reset': 'earliest',
}


consumer = Consumer(CONSUMER_CONFIG)
consumer.subscribe(['weather'])


while True:
    msg = consumer.poll(2)
    if msg:
        data = pickle.loads(msg.value())
        print(data)


