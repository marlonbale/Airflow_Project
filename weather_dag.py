from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from main import weather_etl

#step 1: create dag arguments
default_args = {
    'owner': 'Marlon',       #responsible for DAG
    'depends_on_past':False,    #Whether the tasks depend on the success of previous runs?
    'start_date': datetime(2023, 8, 29), #When the DAG should start running
    'retries': 1,  #How many times a task should retry in case of failure.
    'retry_delay': timedelta(minutes=5), #How long to wait between task retries
}


#Step 2: Creating the DAG instance

dag =  DAG(
    'weather_etl_dag',
    default_args = default_args,
    description = 'DAG to extract weather data',
    schedule_interval = timedelta(days=1),
)


#calling pythonOpertors
run_etl = PythonOperator(
    task_id= 'weather_etl',
    python_callable= weather_etl,
    dag=dag, 
 )

run_etl






