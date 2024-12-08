students = ["liz", "gabs", "jack", "mike"]
number = [1, 2 ,4 , 7]
info = []

#calculates number of items in list
print(len(students))

#replaces item in list
students[1] = "cas"
print(students)

#adds item to the end of the list
students.append("sofia")
print(students)

#adds item where you want it to be placed in the list
students.insert(3, "laura")
print(students)

#remove specific item from a list
students.remove("laura")
print(students)

#removes last item in the list
students.pop()
print(students)

#removes item in certain index
students.pop(2)
print(students)

#orders the list alphabetically
students = ["liz", "gabs", "jack", "mike"]
students.sort()
print(students)

#similarly: it sorts the numbers smallest to largest
numbers = [1, 3, 5, 2, 3]
numbers.sort()
print(numbers)

#how to sort numbers largest to smallest
numbers.sort(reverse=True)
print(numbers)





# Create a list of 3 countries you’d like to visit
# Print out the list
# Remove the last country
# Print out the list
# Add another element at the beginning of the list
# Print out the list
# Print out the length of the list
# Sort the list 
# Print out the list



countries = ["England", "France", "Spain"]
print(countries)
countries.pop()
print(countries)
countries.insert(0, "Italy")
print(countries)
print(len(countries))
print(countries)
countries.sort()
print(countries)



