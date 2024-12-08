city = input("What is your city name? ")
city = city.capitalize()
temperature = input("What is the current temperature in your city? ")
if city and temperature:
    temperature = int(temperature)

    if temperature > 20:
        print(f"It is currently warm in {city} with a current temperature of {temperature} degrees celsius")
    elif temperature > 10:
        print(f"It is currently chilly in {city} with a temperature of {temperature} degrees celsius")
    else:
        print(f"It is currently cold in {city} with a temperature of {temperature} degrees celsius")
else:
    print("Please try again and enter a city and temperature")
