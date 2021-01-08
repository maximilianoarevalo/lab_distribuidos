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
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
    url = url.format(city_name, api_key)
    request = requests.get(url)
    data = request.json()
    return data

a = get_city_weather(city, api_key)

a = pickle.dumps(a)
print(a)