import json
import os
import requests
from dotenv import load_dotenv
from kafka import KafkaProducer
from time import sleep
#---------------------------------------------------------------------------------------------------


def retrieve_response(
            URL:str,
            key: str,
            host:str)->list:
    """Function returns list of JSON objects from REST API endpoint.
    
       @URL: str - URL of REST API to retrieve items from
       @key: str - API Key of REST API to retrieve items from
       @host: str - Hostname of API to retrieve items from
    """

    headers = {
                "x-rapidapi-key": key,
                "x-rapidapi-host": host
            }

    request = requests.get(URL, headers = headers)

    return json.loads(request.text)



#Loading Environment variables ---

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_HOST = os.getenv("API_HOST")


#Requesting REST API ---

covid_data = retrieve_response(
            URL = "https://who-covid-19-data.p.rapidapi.com/api/data",
            key = API_KEY,
            host = API_HOST
        )



#Sending data to Kafka topic ---

producer = KafkaProducer(
            bootstrap_servers = "localhost:9092",
            value_serializer = lambda message: json.dumps(message).encode("utf8")
        )


for record in covid_data:
    sleep(3)
    producer.send("covid_data", record)















