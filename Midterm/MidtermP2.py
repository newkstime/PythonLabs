import random

list1 = []
list2 = []
list3 = []
list4 = []
big_list = []
oddList = []
evenList = []
#a)
for i in range(6):
    num = random.randint(10,20)
    list1.append(num)
print("List 1:", list1)
#b)
for i in range(6):
    num = random.randint(15,25)
    list2.append(num)
print("List 2:", list2)
#c)
list3 = list1[:3] + list2[-3:]
print("List 3:", list3)
#d)
list4 = list1[-3:] + list2[:3]
print("List 4:", list4)
#e)
list3.sort()
print("List 3 sorted in ascending order:", list3)
#f)
list4.sort()
list4.reverse()
print("List 4 sorted in descending order:", list4)
#g)
big_list = [list3, list4]
print("Big List:", big_list)
#h)
print("Numbers in big list:")
for row in range(2):
    for col in range(6):
        print(big_list[row][col])
#i)
oddList = [x for x in list3 if x % 2 != 0]
print("Odd numbers in List 3:", oddList)
#j
evenList = [x for x in list4 if x % 2 == 0]
print("Odd numbers in List 4:", evenList)
