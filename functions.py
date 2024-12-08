def city_info():
  city_name = input("what city are you in right now?" )
  temperature = int(input("what is the current temperature?" ))
  
  if city_name == "" or temperature == "":
      print("error")
  else:
      print(f"You are in {city_name} and the temperature is {temperature} degrees celsius")
         
city_info()
city_info()