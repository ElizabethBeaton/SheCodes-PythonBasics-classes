"""
    What is a rest api?
    its what allows us to communicate to oher services
    you can write some code and communicate with another piece of code somewhere on the internet and get some inf and do something with this info
    eg a bank transfering somehting, the bank will have their own api and we can get this through code
    click ( you )
    makes a http request to a url. we ask the url something and thisll be sent to a server and this server will give you back a json (dictionary /object) which has info
    
    """ 
#first i had to write pip3 install requests into terminal to import this package
import requests

#get the api response
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
#above, at the end i wrote '1'. you dont normally write this. i just did for it to show one one to do list. if you dont write 1, it will show you all of the to do list dictionaries

#this printed out '<Response [200]>' whc=ich means it has loaded successfully. 400 would mean we werent authorised to get anything or couldnt find anything

#so how do we convert this into json/dictionary? this will give you back a list or dictionary
#first we write:
todo = response.json()
print(todo)
print(todo['title'], todo['completed'])