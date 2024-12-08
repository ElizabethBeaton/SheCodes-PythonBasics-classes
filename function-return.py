def full_name(first_name, last_name, middle_name=None):
  """Generate full name from first and last name"""
  if middle_name:
    return first_name + " " + middle_name + " " + last_name
  else:
    return first_name + " " + last_name


name = full_name("John", "Doe")
print("The full name is " + name)
name = full_name("John", "Doe", "Jr.")
print("The full name is " + name)











temperature = 15
city = "London"
print(f"It is currently {temperature}ºC in {city}")

def temperature(celsius_temp, city_name,):
    
    fahrenheit_temp = ({celsius_temp} * 9 / 5) + 32  
    return fahrenheit_temp

temperature = (15, "London")
print(f"It is currently {celsius_temp} degrees ({fahrenheit_temp}) degrees in {city_name} ")

    