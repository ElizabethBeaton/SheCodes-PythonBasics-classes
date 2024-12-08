students = ["liz", "gabs", "jack", "mike"]

for student in students:
    if student != 'gabs':
        print(f"The student's name is {student.title()}.")
        
        
        
#HW: 
# Create a new Repl
# Create a list of 3 countries you’d like to visit.
# Loop through each country and print out the following sentence with the correct country and the correct number
# My number 1 country is Canada
# My number 2 country is Brazil
# My number 3 country is Japan

countries = ["Cambodia", "South Africa", "Ecuador"]

index = 0
for country in countries:
    print(f"My number 1 country is {country}")
    index += 1
    
    