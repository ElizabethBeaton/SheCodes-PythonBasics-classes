#you need to include this otherwise wont work when writing date
from datetime import datetime

#get current date and time
now = datetime.now()
print(now)

#how to create a date manually
date = datetime(2027, 1, 24, 4, 0, 12)
print(date)

#convert a date to  string
formatted_date = date.strftime("See you on %d/%m/%Y, %H:%M:%S")
print("The date and time of the event is: " + formatted_date)

#get a timestamp from a date
print(now.timestamp())

#create a date from a timestamp
timestamp = 1705640834.671713
date_from_timestamp = datetime.fromtimestamp(timestamp)
print(date_from_timestamp)
