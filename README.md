# Airflow_Project
Basic hands on project that involves ETL (Extract,Transfer,Load) and Airflow DAG(Directed Acyclic Graph).


# Introduction & Goals
In this project goal is to understand ETL (Extract,Transfer,Load) process and also understanding Airflow DAG (Directed Acyclic Graph). This project will be also carried out on AWS cloud platform.

## Table of Contents
1. [Introduction](#Introduction)
2. [Project Overview](#project-overview)
3. [Dependencies and Tools](#dependencies-and-tools)
4. [Project Excecution](#project-execution)
5. [Building and Pushing the Docker Image](#building-and-pushing-the-docker-image)
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
![Architecture](Airflow_Project
/architecture.png)


1. Wrote a simple Flask web application: Started by creating a basic Flask web application using Python. Flask is a beginner-friendly web framework that allows you to build web applications easily.
2. Defined the Python dependencies: In project directory, created a file called requirements.txt. This file is to list all the Python libraries and dependencies the Flask application requires. These libraries are like building blocks that provide additional functionality to your application.
3. Create a Dockerfile: In the same project directory, created a file called Dockerfile. This file will contain instructions for building the Docker image.
4. Build the Docker image: Once Flask application code and requirements.txt file was created , next step was to build the Docker image. Terminal or command prompt to navigate to the project directory, and run the command to build the image. Docker will use the instructions in the Dockerfile to build an image that includes application code and its dependencies.


## Building and Pushing the Docker Image:
To build and push the Docker image to a registry, The below are the steps taken:

1. Log in to the Docker registry using `docker login`.
2. Build an Image using : **docker build -t flask-app-image .** (This command builds the Docker image using the Dockerfile and tags it as flask-app-image.)
3. Run the Docker container based on the image using the following command:
   **docker run -p 5000:5000 flask-app-image**
This command starts the Docker container and maps port 5000 of the container to port 5000 of our local machine.
Flask application could be accessed by visiting http://localhost:5000 in our web browser and we should see the "Hello, Docker!" message displayed.
By following these steps, Flask application will be running inside a Docker container and accessible through local machine's port 5000.

#Additional:
1. Created a repository and pushed the image into it by:
     1. **docker tag flask-app-image marlondockerb/flaskapp:v1.0**
     2. **docker push marlondockerb/flaskapp:v1.0**


## Conclusion
In this project, we demonstrated how to containerize a Python application using Docker. By containing the application and its dependencies in a Docker image, we can make sure a  consistent and reliable execution across different environments. 
Docker allows for easier deployment and distribution of applications, making it a valuable tool for modern software development and deployment processes.

# Follow Me On
[LinkedIn](https://www.linkedin.com/in/marlon-balasuriya-479309b5/)
