def display_info(city_name, temperature, humidity_level=""):
    """retrieving info from the user """
    if humidity_level:
        info = (f"The temperature in {city_name} is {temperature} degrees with a humidity of {humidity_level}%")
    else:
        info = (f"The temperature in {city_name} is {temperature} degrees")
    print(info)

display_info("London", 7, 40)
display_info("New York", 10)
        

        