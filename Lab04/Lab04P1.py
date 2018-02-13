another = "y"
while another == "y":
    fpg = float(input("Please enter the patient's fasting plasma glucose level:"))
    while fpg < 0:
        print("FPG cannot be a negative number.")
        fpg = float(input("Please enter the patient's fasting plasma glucose level:"))
    if fpg > 125:
        print("The patient has diabetes.")
    elif fpg > 100:
        print("The patient is pre-diabetic.")
    else:
        print("The patient has a healthy fpg level.")
    another = input("Check another patient's fpg level? [y/n]")
    while another != "y" and another !="n":
        print("Invalid input")
        another = input("Check another patient's fpg level? [y/n]")
