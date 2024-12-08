# Import datetime
# Display the current date and time (no formatting)
# Display the current date and time following this format: Date: Jan 12, 2032 Time: 14:03
# Convert this time stamp 1705590204 into a date and display only the time using this format: 2:30am

from datetime import datetime

now = datetime.now()
print(now)

date = datetime(2024, 11, 12, 15, 5)

formatted_date = date.strftime("Date %b %-d, %Y Time: %-H:%M")
print(formatted_date)

timestamp = 1705590204
date_from_timestamp = datetime.fromtimestamp(timestamp)
print(date_from_timestamp.strftime("%-I:%M%p"))


#another way: 

# timestamp_datetime = datetime.fromtimestamp(1705590204)
# print(timestamp_datetime)

# formatted_timestamp_datetime = timestamp_datetime.strftime("%-I:%M%p")
# print(formatted_timestamp_datetime.lower())


