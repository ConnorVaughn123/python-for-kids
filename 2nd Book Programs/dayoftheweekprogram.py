# day of the week program
day = input('Enter day of the week: ')
if day == 'Monday' or day == 'Wednesday':
    alarm = '7:30 AM'
    carpool = True
    codingclass = True
    gym = False
elif day == 'Tuesday' or day == 'Thursday':
    alarm = '7:30 AM'
    carpool = False
    codingclass = False
    gym = True
elif day == 'Friday':
    alarm = '6:30 AM'
    carpool = True
    codingclass = False
    gym = False
else:
    alarm = 'OFF'
    carpool = False
    codingclass = False
    gym = True
print(alarm, carpool, codingclass, gym)
