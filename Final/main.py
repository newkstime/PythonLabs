from customer import Customer

customer1_email = input("Please enter the email address of the first customer: ")
customer1 = Customer(customer1_email)
customer1.input_info()
customer1.verify_info()

customer2_email = input("Please enter the email address of the next customer: ")
customer2 = Customer(customer2_email)
customer2.input_info()
customer2.verify_info()

output_file = open("customers.txt", 'w')
output_file.write(customer1.output_info())
output_file.write(customer2.output_info())
output_file.close()
