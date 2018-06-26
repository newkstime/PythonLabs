import re

user_input = input("Enter a string:")
user_input = user_input.upper()
user_input = re.sub("[^a-zA-Z]","", user_input)
occurs_dict = {}
for n in user_input:
    keys = occurs_dict.keys()
    if n in keys:
        occurs_dict[n] += 1
    else:
        occurs_dict[n] = 1

print("Dictionary:", occurs_dict)

find_count = input("Choose a letter:")
find_count = re.sub("[^a-zA-Z]","", find_count)
find_count = find_count.upper()
if find_count not in occurs_dict.keys():
    print("Value not in dictionary.")
    quit()
print("The letter", find_count, "appears", occurs_dict[find_count], "times.")
del occurs_dict[find_count]
print("Dictionary after removing", find_count, ":", occurs_dict)

letter_list = list(occurs_dict.keys())
print("Letters sorted:", sorted(letter_list))
