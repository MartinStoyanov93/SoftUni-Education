# Write a program which receives a single string containing numbers separated by a single space.
# Print a list containing the opposite of each number.


string_of_numbers = input()
list = []
modified_list = []

for el in string_of_numbers.split(" "):
    list.append(el)

for i in range(0, len(list)):
    list[i] = int(list[i])

for j in list:
    modified_list.append(-j)

print(modified_list)

