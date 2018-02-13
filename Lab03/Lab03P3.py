print("Please enter in three numbers.")
number1 = float(input("First number:"))
number2 = float(input("Second number:"))
number3 = float(input("Third number:"))
if number1 >= number2 and number1 >= number3:
    print(number1, "is the largest number.")
elif number2 >= number3:
    print(number2, "is the largest number.")
else:
    print(number3, "is the largest number.")
