time = input("Enter 24hr time in HH:MM:SS format:")
colons = time.count(':')
while colons != 2:
    print("Incorrect format, please utilize exact format.")
    quit()

timeNoColons = time.replace(":", "")
timeNotNumbers = timeNoColons.isdigit()
if timeNotNumbers == False:
    print("Please use only numbers for time values.")
    quit()

def twoDigitCheck(value):
    if len(value) == 2:
        return True
    else:
        return False

timeBreakUp = time.split(":")
hours = int(timeBreakUp[0])
minutes = int(timeBreakUp[1])
seconds = int(timeBreakUp[2])

for value in timeBreakUp:
    if twoDigitCheck(value) == False:
        print("Incorrect format. Please enter values in two digit format (e.g. \"04:15:09\")")
        quit()

if hours < 0 or hours > 23:
    print("Hours value must be between 0 and 23.")
    quit()

if minutes < 0 or minutes > 59:
    print("Minutes value must be between 0 and 59.")
    quit()

if seconds < 0 or seconds > 59:
    print("Seconds value must be between 0 and 59.")
    quit()

print(timeNoColons)
