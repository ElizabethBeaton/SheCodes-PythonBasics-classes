#collect the data
first_name = input("What is your name? ")
city = input("What city do you live in currently? ")
celsius_temperature = input(f"What is the temperature in you {city}? ")

#calculations for fahrenheit
fahrenheit_temperature = (float(celsius_temperature) * 9/5) + 32
fahrenheit_temperature = round(fahrenheit_temperature)

#display welcome message
welcome_message = f"Hi {first_name.capitalize()}, you are in {city.capitalize()} and it is currently {celsius_temperature}C or {fahrenheit_temperature}F"
print(welcome_message)

#calculate tonights temperature
tonight_celsius_temperature = int(celsius_temperature) - 10
tonight_fahrenheit_temperature = (float(tonight_celsius_temperature) * 9/5) + 32
tonight_fahrenheit_temperature = round(tonight_fahrenheit_temperature)

prediction_message = f"I predict that tonight, the temperature will reach {tonight_celsius_temperature}C or  {tonight_fahrenheit_temperature}F"

print(prediction_message)
print("Have a good day !")




#similarly:
name = input("What is your name? ")
city = input("What city do you live in? ")
temp_in_celsius = input("What is the temperature in celsius in your city right now? ")
temp_in_fahrenheit = (int(temp_in_celsius) * 9/5) + 32
new_temp_celsius_prediction = (int(temp_in_celsius) - 10)
new_temp_fahrenheit_prediction = (int(new_temp_celsius_prediction) * 9/5) + 32

print(f"Hi {name}, you are in {city}, and it is currently {temp_in_celsius} degrees or {temp_in_fahrenheit} degress fahrenheit.")
print(f"I predict that tonight, the temperature will reach {new_temp_celsius_prediction} degrees or {new_temp_fahrenheit_prediction} degrees fahrenheit")
print("Have a good day!")