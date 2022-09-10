# You will receive a single number n. On the next n lines you will receive integers.
# After that you will be given one of the following commands:
# ⦁	even
# ⦁	odd
# ⦁	negative
# ⦁	positive
# Filter all the numbers that fit in the category (0 counts as a positive and even). Finally, print the result.

number = int(input())
storage_list = []
filtered_list = []
count = 0

while not count == number:
    num = int(input())
    storage_list.append(num)
    count += 1

if count == number:
    command = input()
    for el in storage_list:
        if command == "even":
            if el % 2 == 0:
                filtered_list.append(el)
        if command == "odd":
            if not el % 2 == 0:
                filtered_list.append(el)
        if command == "positive":
            if el >= 0:
                filtered_list.append(el)
        if command == "negative":
            if el < 0:
                filtered_list.append(el)

print(filtered_list)




