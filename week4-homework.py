weather = {
  "city":"Lisbon",
  "country":"Portugal",
  "temperature": 17.94,
  "humidity":77
}
celsius_temperature = weather['temperature']
celsius_to_fahrenheith =  (celsius_temperature * 9/5) + 32
# Display the weather in Lisbon such as:
# It is 18ºC (64ºF) in Lisbon, Portugal, the humidity level is 77%.
print(f"It is {weather['temperature']}C ({celsius_to_fahrenheith}F) in {weather['country']}, {weather['city']}, the humidity level is {weather['humidity']}% ")


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

print(f"The forecast for {forecast['city']}, {forecast['country']} for the next 5 days is :")
index = 0
for daily in forecast.items():
    print(f"Day {index + 1}: {forecast['daily'][index]}")
    index = index + 1
    
    
    
