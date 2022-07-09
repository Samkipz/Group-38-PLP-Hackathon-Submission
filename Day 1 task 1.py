""" Bus Fare Challenge – Task One (Day 1) """


import time

date = time.strftime("%Y-%m-%d") # get todays date and format as yyyy/mm/dd

day = time.strftime("%a") # Uses today's date to get the name on the day of the week(Abbreviated)


#Determine the today's fare following these bus fare schedule
"""
	Monday - Friday --> 100
	Saturday --> 60
	Sunday --> 80
"""

# we shall use the logic, if today is not Sat or Sun, fair == 100.
if day == 'Sat':
    fare = 60
elif day == 'Sun':
    fare = 80
else:
    fare = 100

print("Date: ",date)
print("Day: ",day)
print("Fare: ",fare)