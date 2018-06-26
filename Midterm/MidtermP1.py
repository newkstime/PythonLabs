carType = input("Please select your car type.\nEnter [C] for Compact.\nEnter [M] for Midsize.\nEnter [F] for Fullsize.\n").lower()
if carType !="c" and carType !="m" and carType !="f":
    print("Invalid car type. Program ended.")

daysRented = int(input("Please enter how many days you will be renting:"))
if daysRented <= 0:
    print("Invalid number of days. Program ended.")

fullPriceDays = 3
compactRate = 30
compactDiscount = 26
midsizeRate = 37
midsizeDiscount = 32
fullsizeRate = 45
fullsizeDiscount = 38


if carType == "c":
    rentalFee = compactRate * daysRented
    if daysRented > fullPriceDays:
        rentalFee = (compactRate * fullPriceDays) + (compactDiscount * (daysRented - fullPriceDays))

elif carType == "m":
    rentalFee = midsizeRate * daysRented
    if daysRented > fullPriceDays:
        rentalFee = (midsizeRate * fullPriceDays) + (midsizeDiscount * (daysRented - fullPriceDays))

elif carType == "f":
    rentalFee = fullsizeRate * daysRented
    if daysRented > fullPriceDays:
        rentalFee = (fullsizeRate * fullPriceDays) + (fullsizeDiscount * (daysRented - fullPriceDays))

print("Rental Fee:", rentalFee)
