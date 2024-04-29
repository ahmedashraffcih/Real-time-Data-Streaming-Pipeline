from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from data_generation.stream_data import stream_data

default_args = {
    'owner': 'Ahmed Ashraf',
    'start_date': datetime(2024, 2, 2, 10, 00)
}

with DAG('user_automation',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:
    streaming_task = PythonOperator(
        task_id='stream_from_api',
        python_callable=stream_data
    )
