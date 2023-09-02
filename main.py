import requests
import pandas as pd
import json
from datetime import datetime
import s3fs

def weather_etl():
    api_key = "553fea112a6b41****"
    city = 'New_York'
    end_point = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'


    #make the API requests
    response = requests.get(end_point)
    data = response.json()

    #print(data)

    #data we need
    location = data['location']['name']
    temperature_c = data['current']['temp_c']

    weather_list = []

    weather_data = {"location": location,
        "temperature_c": temperature_c,
    }

    print(weather_data)

    weather_list.append(weather_data)

    #create  a pandas dataframe

    df = pd.DataFrame(weather_list)
    #df.to_csv("NYC_data.csv")
    
    #saving the csv to s3bucket
    df.to_csv("s3://marlon-airflow-bucket/NYC_data.csv")









