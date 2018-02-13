shipMethod = str.lower(input("Please select your shipping method. Enter S of standard shipping or E for express shipping:"))
if shipMethod != "s" and shipMethod != "e":
    print("Invalid shipping method value.")
packageWeight = float(input("Please enter in the weight of the package in pounds:"))
if shipMethod == "s":
    if packageWeight <= 4:
        cost = packageWeight *1.05
    elif packageWeight > 4 and packageWeight <= 8:
        cost = packageWeight *0.95
    elif packageWeight > 8 and packageWeight <= 15:
        cost = packageWeight *0.85
    elif packageWeight > 15:
        cost = packageWeight * 0.80
elif shipMethod == "e":
    if packageWeight <= 4:
        cost = packageWeight * 3.25
    elif packageWeight > 4 and packageWeight <= 8:
        cost = packageWeight * 2.95
    elif packageWeight > 8 and packageWeight <= 15:
        cost = packageWeight * 2.75
    elif packageWeight > 15:
        cost = packageWeight * 2.55
print("Shipping charge: $", "%.2f" % cost)
