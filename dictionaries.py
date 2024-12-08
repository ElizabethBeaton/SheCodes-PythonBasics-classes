#creating a dictionary with key value pairs
temperatures = {"lisbon": 12, "Paris": 5, "london": 9}

print(temperatures)

#creating an empty dictionary
winners = {}
print(winners)

#accessing a value. We use square brackets to access the dictionary
print(temperatures["Paris"])
#with dictionaries, the order does not matter like it does in lists

#adding a new key-value pair
temperatures["New York"] = 2
print(temperatures)

#modify a value
temperatures["Paris"] = 25
print(temperatures["Paris"])

#removing key value pair
del temperatures["lisbon"]
print(temperatures)
#another way to do this
temperatures.pop("Paris")
print(temperatures)

students = {
    1: {"first_name": "Maria",
        "last_name": "Jones",
        "country": "England",
        "graduated": True
        },
    2: {
        "first_name": "Lizzie",
        "last_name": "Beaton",
        "country": "Germany",
        "certificated": ["Plus", "Basics", "Python"]
    }
}
print(students)


countries_to_visit = {"France": "Paris", "Spain": "Barcelona", "Germany": "Hamburg"}
print(countries_to_visit)
del countries_to_visit["France"]
print(countries_to_visit)
countries_to_visit["America"] = "Washington"
print(countries_to_visit)

print("The capital city of Spain is " + countries_to_visit["Spain"])
print("The capital city of Germany is " + countries_to_visit["Germany"])
