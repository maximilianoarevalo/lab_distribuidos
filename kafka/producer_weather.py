from confluent_kafka import admin, Producer
import requests
import pickle
import json


city = "santiago"
api_key = "e9185b28e9969fb7a300801eb026de9c"


KAFKA_CONFIG = {
    "bootstrap.servers": "localhost:9092"
}


def get_city_weather(city_name, api_key):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric"
    url = url.format(city_name, api_key)
    request = requests.get(url)
    data = request.json()
    return data


calls = 0
kafka_client = admin.AdminClient(KAFKA_CONFIG)
new_topic = admin.NewTopic("weather", 1, 1)
kafka_client.create_topics([new_topic])
producer = Producer(KAFKA_CONFIG)
while True:
    query = get_city_weather(city, api_key)
    if query["cod"] != 200:
        print("error")
        break
    else:
        producer.produce("weather", pickle.dumps(query))
    time.sleep(1800)
