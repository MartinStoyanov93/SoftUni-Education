# Write a program that receives two numbers (factor and count) and creates a list with length of the given count
# and contains only integer numbers that are multiples of the given factor. The numbers should be only positive,
# and they should be arranged in ascending order, starting from the smallest multiple number.

count_num1 = int(input())
len_num2 = int(input())

list = []

for i in range(1, len_num2 + 1):
    list.append(count_num1 * i)

print(list)