# Airflow_Project
Basic hands on project that involves ETL (Extract,Transfer,Load) and Airflow DAG(Directed Acyclic Graph).


# Introduction & Goals
In this project goal is to understand ETL (Extract,Transfer,Load) process and also understanding Airflow DAG (Directed Acyclic Graph). This project will be also carried out on AWS cloud platform.

## Table of Contents
1. [Introduction](#Introduction)
2. [Project Overview](#project-overview)
3. [Dependencies and Tools](#dependencies-and-tools)
4. [Project Excecution](#project-execution)
5. [Setting up in Airflow using EC2 instance](#Setting-up-in-Airflow-using-EC2-instance)
6. [Conclusion](#conclusion)

## Project Overview

The project is mainly focused on extracting data from a weather API using python,use python to transform data, deploy the code on Airflow/EC2 and save the final result on Amazon S3.

The ETL process:
1. Extract: In this step of data we get data from an external sourcein which case is a weather API. Goal is to extract weather data of a city (NYC in this case) and get the temperature.
2. Load: Once the data is being extracted using python we will be organizing the data to be used and will be cleaning the data that we would be recieving as a JSON and formating it.
3. Load: Once the data is ready and cleaned the goal is to store it in a structural format such as a csv file or a databse.

Airflow and DAG:
Airflow could be considered and workflow orchestration tool where you can build, schedule and monitor data pipleines. Workflow here basically means the sequence of every task. In Airflow it is known as a DAG. As a visual representation of the workflow for an ETL process. It defines the order in which different tasks are executed. Each task performs a specific job in the ETL process.


## Dependencies and Tools:
- Python: Data is exrtracted using an API and we used Pandas, to store data in that Datframe and later create a csv.
- Airflow: workflow orchestration tool
- Amazon EC2: Virtual Machine or an instance and deploy airflow.
- Amazon S3 bucket: To save dataframe created in main.py

## Project execution
![Architecture](https://github.com/marlonbale/Airflow_Project/blob/main/Architecture.png)

The above image shows the architecture in order to achieve this project.

1. In the [main.py](main.py) a function is created ("weather_etl) that retrieves current weather data for New York city, processes it and saces it as a csv file in an Amazon S3 bucket so that it can be easily shared and accessed by others.
   
**Importing necessary Python libraries**
import requests  # Allows us to make internet requests
import pandas as pd  # Helps us work with data effectively
import json  # Used for working with data in a special format
from datetime import datetime  # Helps with date and time operations
import s3fs  # Allows us to interact with cloud storage

2. In the [weather_dag.py](weather_dag.py) the following  were done.
   
**step1:**
  from datetime import timedelta
  from airflow import DAG
  from airflow.operators.python_operator import PythonOperator
  from datetime import datetime
  from main import weather_etl

We are setting up necessary components working with Apache airflow a tool for     scheduling and running data workflows.Import the weather_etl function from a Python file named main. This function is the one we explained earlier, responsible for getting and processing weather data.

**step 2: Creating a DAG instance:**
   Define default arguments for the DAG
  default_args = {
      'owner': 'Marlon',               # Person responsible for the DAG
      'depends_on_past': False,        # Whether tasks depend on the success of previous runs
      'start_date': datetime(2023, 8, 29),  # When the DAG should start running
      'retries': 1,                   # How many times a task should retry in case of failure
      'retry_delay': timedelta(minutes=5),  # How long to wait between task retries
  }
  
  Create the DAG instance
  dag = DAG(
      'weather_etl_dag',                 # Unique identifier for the DAG
      default_args=default_args,         # Use the default arguments defined above
      description='DAG to extract weather data',  # Description of the DAG's purpose
      schedule_interval=timedelta(days=1),      # How often the DAG should run (daily in this case)
  )

Define the DAG with a unique identifier, description, and schedule interval. This DAG is set to run daily (schedule_interval=timedelta(days=1)).

**step 3: Python Operators**

  Create a PythonOperator called 'run_etl'
  run_etl = PythonOperator(
      task_id='weather_etl',         # Unique identifier for this task
      python_callable=weather_etl,   # The Python function to execute (weather_etl function)
      dag=dag,                       # The DAG to which this task belongs
  )
  
  Add the 'run_etl' task to the DAG
  run_etl

In this step we are defining a pythonOpearor called run_etl:
task_id is a unique identifier for this task.
python_callable specifies the Python function that this task will execute, which is the weather_etl function we explained earlier.
dag indicates which DAG this task belongs to, and it's set to our dag variable, which is our weather extraction DAG.
This operator will run the weather_etl function as a task within our DAG, extracting and processing weather data.


## Setting up in Airflow using EC2 instance:
Setting up Airflow in EC2 instance could be a multiple process. however once the EC2 is running use ssh to connect and replace the key that you are recieving .
Once we are in the EC2 instace we have to follow several commands to get airflow going on. those are as below:

![EC2](https://github.com/marlonbale/Airflow_Project/blob/main/ec2_instance.png)


sudo apt-get update: to update the packages
sudo apt install python3-pip
sudo apt install apache-airflow
sudo pip install pandas
sudo pip install s3fs
sudo pip install datetime
sudo pip install requests

once the airflow is being installed you can open airflow using airflow standalone.

**Create and Run Airflow DAGs:**
1.Create your Airflow DAGs (workflow definitions) in the ~/airflow/dags directory on your EC2 instance.
2.You can use any text editor or an integrated development environment (IDE) to create DAG Python files.
3.To run a DAG, you can trigger it manually from the Airflow web interface.Access the Airflow web interface at http://your-ec2-public-ip:8080. Here, you can monitor, manage, and trigger your DAGs.

![Airflow](https://github.com/marlonbale/Airflow_Project/blob/main/Airflow_local.png)

![Airflow](https://github.com/marlonbale/Airflow_Project/blob/main/Airflow_DAGS.png)

Weather_dag:
![Airflow](https://github.com/marlonbale/Airflow_Project/blob/main/weather_DAG.png)

**Saving data on s3 bucket:**

![Airflow](https://github.com/marlonbale/Airflow_Project/blob/main/s3bucket.png)





## Conclusion
Main lesson learnt was that Airflow is a great tool for orchestration, coding DAG was very straight forward. Task flow seems to be very straightforward as well. (Expanding this project to cloud platforms was because hosting airflow locally and using docker container kept failing.)

# Follow Me On
[LinkedIn](https://www.linkedin.com/in/marlon-balasuriya-479309b5/)
