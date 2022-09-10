import sys
num = int(input())

max_number = -sys.maxsize
sum = 0

for i in range(num):
    number = int(input())

    if number > max_number:
        max_number = number

    sum += number

total_sum = sum - max_number

result = 0
if total_sum == max_number:
    print("Yes")
    print(f"Sum = {total_sum}")
else:
    result = max_number - total_sum
    print("No")
    print(f"Diff = {abs(result)}")
