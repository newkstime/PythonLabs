import random
listOne = []
for x in range (5):
    listOne.append(random.randint(1,9))
print("First list:", listOne)

listTwo = []
for x in range (5):
    listTwo.append(random.randint(2,8))
print("Second list:", listTwo)

for i in range(len(listOne)):
    if listOne[i] > listTwo[i]:
        print(listOne[i])
    else:
        print(listTwo[i])
