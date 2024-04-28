from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from kafka import KafkaProducer
from kafka import KafkaConsumer
import json 
import time 
import logging
import psycopg2
import threading

def get_data():
    import requests
    
    res = requests.get('https://randomuser.me/api/')
    res = res.json()
    res = res['results'][0]

    return res

def format_data(res):
    data = {}
    location = res['location']
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']
    data['address'] = f"{str(location['street']['number'])} {location['street']['name']}, " \
                      f"{location['city']}, {location['state']}, {location['country']}"
    data['post_code'] = location['postcode']
    data['email'] = res['email']
    data['username'] = res['login']['username']
    data['dob'] = res['dob']['date']
    data['registered_date'] = res['registered']['date']
    data['phone'] = res['phone']
    data['picture'] = res['picture']['medium']

    return data

def stream_data():

 # Creating Kafka Producer
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

def load_data():
    # Establishing connection to SQL Server
    conn = psycopg2.connect(
        dbname='cust_dwh',
        user='postgres',
        password='1234',
        host='localhost',
        port='5432'
    )
    cursor = conn.cursor()

    # Creating Kafka Consumer
    consumer = KafkaConsumer('users_created', bootstrap_servers=['localhost:9092'])
    

    # Extracting data fields
    
    # Continuously consume messages from the topic
    for message in consumer:
        try:
            # Decode message value from bytes to string and parse as JSON
            message_data = json.loads(message.value.decode('utf-8'))

            # Extracting data fields
            first_name = message_data['first_name']
            last_name = message_data['last_name']
            gender = message_data['gender']
            address = message_data['address']
            post_code = message_data['post_code']
            email = message_data['email']
            username = message_data['username']
            dob = message_data['dob']
            registered_date = message_data['registered_date']
            phone = message_data['phone']
            picture = message_data['picture']

            # Inserting data into PostgreSQL table
            cursor.execute("INSERT INTO Users (first_name, last_name, gender, address, post_code, email, username, dob, registered_date, phone, picture) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                           (first_name, last_name, gender, address, post_code, email, username, dob, registered_date, phone, picture))
            conn.commit()
            print("Inserted data:", message_data)
        except Exception as e:
            logging.error(f'An error occurred while processing message: {e}')
            continue

    # Closing PostgreSQL connection
    conn.close()

# Main function to run producer and consumer
if __name__ == "__main__":
    # Start the producer in a separate thread
    producer_thread = threading.Thread(target=stream_data)
    producer_thread.daemon = True
    producer_thread.start()

    # Consume and insert messages into SQL Server
    load_data()