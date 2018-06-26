print("This program creates a list of odd numbers in the range of your choice.")
start_num = int(input("Enter a starting number: "))
end_num = int(input("Enter ending number: "))
oddNumbers =  [i for i in range(start_num, end_num+1) if i % 2 == 1 ]
print("Odd numbers in the range:", oddNumbers)
