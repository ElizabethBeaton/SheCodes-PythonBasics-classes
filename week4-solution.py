
def convert_celsius_to_fahrenheit(celsius_temperature):
    fahrenheith_temperature = temperature * 9/5 + 32
    return fahrenheith_temperature 


weather = {
  "city":"Lisbon",
  "country":"Portugal",
  "temperature": 17.94,
  "humidity":77
}

city = weather["city"]
country = weather["country"]
temperature = weather["temperature"]
humidity = weather["humidity"]
fahrenheith_temperature = convert_celsius_to_fahrenheit(temperature)
print(f"It is {round(temperature)}ºC ({round(fahrenheith_temperature)}ºF) in {city}, {country}, the humidity level is {humidity}%.")



forecast = {
  "city":"Lisbon",
  "country":"Portugal",
  "daily":
    [
      17.76,
      13.08,
      12.14,
      11.25,
      14.29
    ]
}

# Display the forecast in Lisbon such as:
# The forecast for Lisbon, Portugal for the next 5 days is:
# Day 1: 18ºC
# Day 2: 13ºC
# Day 3: 12ºC
# Day 4: 11ºC
# Day 5: 14ºC

city = forecast["city"]
country = forecast["country"]

print(f"The forecast for {city}, {country} for the next 5 days is:")
print(forecast['daily'])
index = 0
for temperature in forecast['daily']:
    fahrenheit_temperature = convert_celsius_to_fahrenheit(temperature)
    print(f"Day {index + 1}: {round(temperature)}C, ({round(fahrenheit_temperature)}F)")
    index = index + 1