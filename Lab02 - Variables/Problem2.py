lab1 = float(input("Input the score for Lab 1:"))
lab2 = float(input("Input the score for Lab 2:"))
lab3 = float(input("Input the score for Lab 3:"))
test1 = float(input("Input the score for Test 1:"))
test2 = float(input("Input the score for Test 2:"))
lab_total = (lab1 + lab2 + lab3)
test_total = test1 + test2
lab_average = (lab_total / 3)
lab_average_weighted = lab_average * .55
test_average = (test_total / 2 )
test_average_weighted = test_average * .45
print("Your final grade is:", lab_average_weighted + test_average_weighted)
