import random
set1 = set()
set2 = set()
for i in range(5):
    number = random.randint(1,10)
    set1.add(number)
for i in range(5):
    number = random.randint(1,10)
    set2.add(number)
print("set1:", set1)
print("set2:", set2)
set_union = set1 | set2
set_odds = {x for x in set_union if x % 2 != 0}
set_intersection = set1 & set2
set_symm_difference = set1 ^ set2
print("Set Union:", set_union)
print("Odd numbers in set union:", set_odds)
print("Set Intersection:", set_intersection)
print("Set Symmetric Difference:", set_symm_difference)

