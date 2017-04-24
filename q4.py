#Question-4 Write a program to print the list after removing all the duplicate values
#List is [12,24,35,24,88,120,155,88,120,155]

old_list = [12,24,35,24,88,120,155,88,120,155]

new_list = []

for numbers in old_list:
    if numbers not in new_list:
        new_list.append(numbers)

print new_list