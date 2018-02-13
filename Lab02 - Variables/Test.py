age = int(input("Enter your age: "))
if age < 12:
    price = 4
elif age < 18:
    price = 7
else:
    price = 10
print("Plase pay this price: ", price)
