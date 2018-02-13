num = range(5, 22, 4)
numList1 = []
for x in num:
    numList1.append(x)
print(numList1)

for x in numList1:
    print(x)

num = range(26, 4, -7)
numList2 = []
for x in num:
    numList2.append(x)
print(numList2)

y = 0
for x in numList1 and numList2:
    y += x
print(y)
