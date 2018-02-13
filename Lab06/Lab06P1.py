#Prompt user for a list of 5 test scores
i = 0
gradeList = []
while i < 5:
    grade = float(input("Please enter the test score: "))
    while grade < 0:
        print("Invalid score")
        grade = float(input("Please enter the test score: "))
    gradeList.append(grade)
    i += 1
print("The scores are", gradeList)
creditList = []
for grade in gradeList:
    if grade < 60:
        grade += 10
        creditList.append(grade)
    else:
        creditList.append(grade)
print("Students who scored below a 60 received 10 extra points.\n", creditList)
print("Students whose scores have changed:")
j = 0
while j < len(gradeList):
    if gradeList[j] != creditList[j]:
        print("Old score:", gradeList[j], " New score:", creditList[j])
        j += 1
    else:
        j += 1

