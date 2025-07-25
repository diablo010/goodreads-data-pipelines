from airflow.decorators import dag, task
from datetime import datetime, timedelta

from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_data

default_args = {
    'owner': 'diablo010',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

@dag(
     dag_id='goodreads_etl_dag',
     default_args=default_args, 
     start_date=datetime(2025, 7, 24),
     schedule='@daily'
)

def goodreads_etl():

    # Wrap imported functions using @task
    extract_task = task()(extract_data)
    transform_task = task()(transform_data)
    load_task = task()(load_data)

    # Task flow
    extract_task() >> transform_task() >> load_task()

dag = goodreads_etl()