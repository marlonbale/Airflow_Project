import requests
import pandas as pd

api_key = "553fea112a6b411f81e204522233107"
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
df.to_csv("NYC_data.csv")









