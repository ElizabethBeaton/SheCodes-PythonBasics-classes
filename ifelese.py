temperature = input("What is the temperature? ")
temperature = int(temperature)
raining = input("Is it raining? yes/no ")
raining = raining.lower()

if temperature > 20 and raining == 'no':
    print("Enjoy a sunny day")
elif temperature > 20 and raining == 'yes':
    print("Don't forget your umbrella")
elif temperature < 20 and raining == 'no':
    print("Don't forget your jacket")
else:
    print("Don't forget your umbrella and your jacket")