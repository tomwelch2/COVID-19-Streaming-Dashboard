import os
import json
import boto3
import pandas as pd
from dotenv import load_dotenv
from kafka import KafkaConsumer
from time import sleep 

#---------------------------------------------------------------------------------------------------


#Retrieving AWS Credentials ---

load_dotenv()

ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
REGION_NAME = os.getenv("AWS_DEFAULT_REGION")
BUCKET_NAME = os.getenv("S3_BUCKET")


#Connecting to S3 ---

S3 = boto3.client(
            service_name = "s3",
            aws_access_key_id = ACCESS_KEY,
            aws_secret_access_key = SECRET_KEY,
            region_name = REGION_NAME
        )



#Retrieving messages from Kafka topic ---

consumer = KafkaConsumer(
            "covid_data",
            bootstrap_servers = "localhost:9092",
            group_id = None,
            auto_offset_reset = "earliest"
        )


messages = []


for message in consumer:
    message = message.value.decode("utf8")
    messages.append(message)
    
    df = pd.DataFrame([json.loads(i) for i in messages])

    df.to_csv("aws_data.csv", mode = "w")

    with open("aws_data.csv", "rb") as f:
        S3.upload_fileobj(f, BUCKET_NAME, "covid_kafka.csv")


