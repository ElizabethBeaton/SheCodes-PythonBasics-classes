"""
    Create a Repl
Ask for a city name
Display the current weather for this specific city such as
It is currently 23ºC in Paris, France”
"""

import requests
from rich import print

city = input("What city would you like to check the weather for? ")
api_key = "1cd294b82d977t5ed35ae2o840f95fe2"
api_url = f"https://api.shecodes.io/weather/v1/current?query={city}&key={api_key}"

response = requests.get(api_url)
weather = response.json()

temperature = weather['temperature']['current']
country = weather['country']

print(f"It is currently {round(temperature)}C in {city}, {country}")

