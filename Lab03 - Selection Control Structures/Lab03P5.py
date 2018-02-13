customerType = str.lower(input("Please your customer type. Enter R for residential or B for business:"))
if customerType != "r" and customerType != "b":
    print("Invalid customer type value.")
    exit()
waterUsage = float(input("Please enter the number of gallons of water used:"))
if waterUsage < 0:
    print("Water usage cannot be a negative amount.")
    exit()
if customerType == "r":
    if waterUsage <= 6000:
        cost = waterUsage * 0.005
    elif waterUsage > 6000:
        cost = ((waterUsage - 6000) * 0.007) + 30
elif customerType == "b":
    if waterUsage <= 8000:
        cost = waterUsage * 0.006
    elif waterUsage > 8000:
        cost = ((waterUsage - 8000) * 0.008) + 48

print("Please pay this amount: $", "%.2f" % cost)
