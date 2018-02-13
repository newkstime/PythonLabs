hour = int(input("Please enter the hour:"))
while hour > 12:
    print("Invalid value for hours.")
    print("Please enter hours in 12 hour format.")
    hour = int(input("Please enter the hours:"))

minutes = int(input("Please enter the minutes:"))
while minutes > 60:
    print("Invalid value for minutes:")
    minutes = int(input("Please enter the minutes:"))

seconds = int(input("Please enter the seconds:"))
while seconds > 60:
    print("Invalid value for seconds:")
    seconds = int(input("Please enter the seconds:"))

am_pm = input("Please enter AM or PM:")
am_pm = am_pm.lower()
while (am_pm != "am" and am_pm != "pm"):
    print("Invalid meridiem")
    am_pm = input("Please enter AM or PM:")
    am_pm = am_pm.lower()

if am_pm == "am":
    if hour == 12:
        hour = 0

if am_pm == "pm":
    if hour != 12:
        hour += 12

hours_in_seconds = hour * 3600
minutes_in_seconds = minutes * 60
total_seconds = hours_in_seconds + minutes_in_seconds + seconds
print("Seconds since midnight:", total_seconds)
