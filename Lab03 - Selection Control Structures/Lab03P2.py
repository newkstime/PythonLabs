secondsSinceMidnight = int(input("Please enter the number of seconds since midnight:"))
seconds = '{:02}'.format(secondsSinceMidnight % 60)
minutesSinceMidnight = secondsSinceMidnight // 60
minutes = '{:02}'.format(minutesSinceMidnight % 60)
hoursSinceMidnight = minutesSinceMidnight // 60
if hoursSinceMidnight < 24 and hoursSinceMidnight >= 12:
    meridiem = "PM"
    hours = hoursSinceMidnight - 12
    if hours == 0:
        hours = 12
    print("The time is ", str(hours) + ":" + str(minutes) + ":" + str(seconds), meridiem)
elif hoursSinceMidnight < 12:
    meridiem = "AM"
    hours = hoursSinceMidnight
    if hours == 0:
        hours = 12
    print("The time is ", str(hours) + ":" + str(minutes) + ":" + str(seconds), meridiem)
else:
    print("The input seconds exceeds the number of seconds in a single day.")
