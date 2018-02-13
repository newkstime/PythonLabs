salary = float(input("Please enter your starting salary:"))
retirement = 0.0
counter = 1
while counter <= 10:
    print ("Year", counter, "salary:", "%0.2f" % salary)
    retirement += (salary * 0.05)
    print ("Retirement Fund total:", "%0.2f" % retirement)
    salary += (salary * 0.02)
    counter += 1
