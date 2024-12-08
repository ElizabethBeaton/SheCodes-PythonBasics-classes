def calculate_fahrenheit_temp(celsius_temp):
  fahrenheit_temp = float(celsius_temp * 9/5) + 32
  return fahrenheit_temp



temperature = 15
fahrenheit_temp = calculate_fahrenheit_temp(temperature)
city = "London"
print(f"It is currently {temperature}ºC  ({fahrenheit_temp}ºF) in {city}")