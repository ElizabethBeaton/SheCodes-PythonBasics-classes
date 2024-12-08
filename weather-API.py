import requests
from rich import print

city = "Madrid"
api_key = "1cd294b82d977t5ed35ae2o840f95fe2"
api_url = f"https://api.shecodes.io/weather/v1/current?query={city}&key={api_key}"

response = requests.get(api_url)
weather = response.json()
#print(weather)


temperature = weather['temperature']['current']
humidity = weather['temperature']['humidity']
wind_speed = weather['wind']['speed']
country = weather['country']
print(f"The temperature in {city}, {country} is currently {round(temperature)}C. The humidity is {round(humidity)}% and the windspeed is {wind_speed}mph")




