def convert_celsius_to_fahrenheit(celsius_value):
    """converts a celsius value into fahrenheit"""
    fahrenheit_value = (float(celsius_value) * 9/5) + 32
    
    return fahrenheit_value


def display_temperature(city_name, temperature):
    """Displays the temp of a city"""
    fahrenheit_temp = convert_celsius_to_fahrenheit(temperature)
    print(f"It is currently {temperature}C ({fahrenheit_temp}F) in {city_name.capitalize()}")


city = input("What is the name of your city? ")
celsius_temp = input(f"Enter the temperature in {city.capitalize()}: ")
display_temperature(city, celsius_temp)