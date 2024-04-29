import sys
sys.path.append("D:/Personal Projects/Realtime Data Streaming/")

from kafka import KafkaProducer
import time 
import logging
import json 
from kafka import KafkaConsumer
from data_generation.get_data import get_data
from data_generation.format_data import format_data
producer = KafkaProducer(bootstrap_servers=['localhost:9092'], max_block_ms=5000)
curr_time = time.time()

while True: 
    if time.time() > curr_time + 60: #1 minute
        break
    try:
        res = get_data()
        res = format_data(res)
        #Sending data to kafka
        producer.send('users_created', json.dumps(res).encode('utf-8'))
        time.sleep(1)
    except Exception as e:
        logging.error(f'An error occured: {e}')
        continue