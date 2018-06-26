import re

class Customer:

    def __init__(self, email):
        self.__last_name = ''
        self.__first_name = ''
        self.__age = 0
        self.__email = email
        self.__password = ''
        self.__card_number = ''
        self.__security_code = ''

    def input_age(self):
        while isinstance(self.__age, int) == False or self.__age <= 0:
            try:
                self.__age = int(input("Enter your age: "))
                while self.__age <= 0:
                    print("ERROR: Age must be a positive value.")
                    self.__age = int(input("Enter your age: "))
            except ValueError:
                print("ERROR: Input must be a positive integer.")

    def input_password(self):
        password_complexity = False
        while password_complexity == False:
            password = input("Choose a password. Passwords must be between 8 and 12 characters long and must contain at least one uppercase letter, one lowercase letter, and one number: ")
            digit_error = re.search(r"\d", password) is None
            uppercase_error = re.search(r"[A-Z]", password) is None
            lowercase_error = re.search(r"[a-z]", password) is None
            if len(password) < 8 or len(password) > 12 or digit_error == True or uppercase_error == True or lowercase_error == True:
                print("Password does not meet complexity requirement.")
                password_complexity = False
            else:
                password_complexity = True
        self.__password = password

    def input_card_number(self):
        card_number = input("Enter your 16 digit credit card number: ")
        while len(card_number) != 16 or card_number.isdigit() == False:
            print("ERROR - Invalid entry.")
            card_number = input("Input your 16 digit credit card number: ")
        self.__card_number = card_number

    def input_security_code(self):
        security_code = input("Enter your 3 digit security code: ")
        while len(security_code) != 3 or security_code.isdigit() == False:
            print("ERROR - Invalid entry.")
            security_code = input("Enter your 3 digit security code: ")
        self.__security_code = security_code

    def input_info(self):
        first_name = input("Please enter your First Name: ")
        while len(first_name) <= 0 or first_name.isalpha() == False:
            print("ERROR - Invalid entry.")
            first_name = input("Please enter your First Name: ")
        self.__first_name = first_name
        last_name = input("Please enter your Last Name: ")
        while len(last_name) <= 0 or last_name.isalpha() == False:
            print("ERROR - Invalid entry.")
            last_name = input("Please enter your Last Name: ")
        self.__last_name = last_name
        self.input_age()
        self.input_password()
        self.input_card_number()
        self.input_security_code()

    def verify_info(self):
        continue_editing = True
        while continue_editing == True:
            print("You have entered the following information: ")
            print("First Name: ", self.__first_name)
            print("Last Name: ", self.__last_name)
            print("Age: ", self.__age)
            print("Password: ", self.__password)
            print("Credit Card Number: ", self.__card_number)
            print("Security Code: ", self.__security_code)
            print("Email address: ", self.__email)
            make_edits = input("Enter [0] to edit your information. Enter [1] to submit information: ")
            if make_edits == "1":
                continue_editing = False
            elif make_edits == "0":
                edit_selection = input("Enter [1] to edit your name. Enter [2] to edit your age. Enter [3] to edit your password. Enter [4] to edit your credit card number. Enter [5] to edit your security code. Enter [6] to edit your email.")
                if edit_selection == "1":
                    first_name = input("Please enter your First Name: ")
                    while len(first_name) <= 0 or first_name.isalpha() == False:
                        print("ERROR - Invalid entry.")
                        first_name = input("Please enter your First Name: ")
                    self.__first_name = first_name
                    last_name = input("Please enter your Last Name: ")
                    while len(last_name) <= 0 or last_name.isalpha() == False:
                        print("ERROR - Invalid entry.")
                        last_name = input("Please enter your Last Name: ")
                    self.__last_name = last_name
                elif edit_selection == "2":
                    self.input_age()
                elif edit_selection == "3":
                    self.input_password()
                elif edit_selection == "4":
                    self.input_card_number()
                elif edit_selection == "5":
                    self.input_security_code()
                elif edit_selection == "6":
                    self.__email = input("Enter your email address: ")
                else:
                    print("ERROR - Invalid Entry.")
            else:
                print("ERROR - Invalid Entry.")
                continue_editing = True

    def output_info(self):
        output_data = (self.__first_name + " " + self.__last_name + " " + str(self.__age) + " " + self.__email + " " + self.__password + " " + self.__card_number + " " + self.__security_code + "\n")
        return output_data
