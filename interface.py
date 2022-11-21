#ex1
import json
import requests
request= "https://api.chucknorris.io/jokes/random"
response = requests.get(request).json()
print(json.dumps(response['value'], indent=2))

#ex2


import requests, json

api_key = "c0c953d7a5a64d118b0551824efc24cc"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter city name : ")
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url).json()
temperature= int(response['main']['temp'])
description= response['weather'][0]['description']
print(f"Current weather in {city_name.capitalize()} is {temperature}°C with a {description}.")



