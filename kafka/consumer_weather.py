from confluent_kafka import Consumer
import pickle
import datetime
from pymongo import MongoClient 
import time


try: 
    conn = MongoClient(
        host=['localhost:27017'],
        document_class=dict,
        username="admin",
        password="retro123",
        connect=True
    ) 
    print("Connected successfully!!!") 
except:   
    print("Could not connect to MongoDB") 

db = conn.ejemplo
collection = db.ejemplo

CONSUMER_CONFIG = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'test',
    'auto.offset.reset': 'earliest',
}

consumer = Consumer(CONSUMER_CONFIG)
consumer.subscribe(['weather'])
i = 0
while True:
    msg = consumer.poll(2)
    if msg:
        data = pickle.loads(msg.value())
        ciudad = data["name"]
        pais = data["sys"]["country"]
        temp = data["main"]["temp"]
        vel = data["wind"]["speed"]
        dt = datetime.datetime.fromtimestamp(data["dt"]).strftime('%Y-%m-%d %H:%M:%S')
        timezone = data["timezone"]
        main = data["weather"][0]["main"]
        pressure = data["main"]["pressure"],
        humidity = data["main"]["humidity"]
        dic = {
            "ciudad": ciudad,
            "pais":pais,
            "temp":temp,
            "vel":vel,
            "date":datetime.datetime.strptime(dt, '%Y-%m-%d %H:%M:%S').date().strftime("%Y-%m-%d"),
            "time":datetime.datetime.strptime(dt, '%Y-%m-%d %H:%M:%S').time().strftime("%H:%M"),
            "main":main,
            "pressure": pressure,
            "humidity":humidity
        }
        collection.insert_one(dic)
    time.sleep(1800)




