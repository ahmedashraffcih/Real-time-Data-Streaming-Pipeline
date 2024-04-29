from kafka import KafkaProducer
import time 
import logging
import json 
from kafka import KafkaConsumer

consumer = KafkaConsumer('users_created', bootstrap_servers=['localhost:9092'])
for message in consumer:
    # Decode message value from bytes to string and parse as JSON
    message_data = json.loads(message.value.decode('utf-8'))
    print(message_data)  # or do whatever processing you need with the message data