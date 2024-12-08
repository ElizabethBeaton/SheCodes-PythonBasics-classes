temperatures = {"Lisbon": 23, "London": 10, "Sydney": 32}

#looping through each key one at a time
for city in temperatures:
    temperature = temperatures[city]
    print(f"The temperature in {city} is {temperature} degrees")
#this would print: 
#The temperature in Lisbon is 23 degrees
#The temperature in London is 10 degrees
#The temperature in Sydney is 32 degrees
    

#looping through each value paid. key, value
#similary to above but this is usually the better way
for city, temperature in temperatures.items():
    print(city)
    print(temperature)
    




