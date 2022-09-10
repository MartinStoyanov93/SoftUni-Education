n = int(input())

even_sum = 0
odd_sum = 0

for i in range(n):
    number = int(input())
    if i % 2 == 0:
        even_sum += number
    else:
        odd_sum += number

if even_sum == odd_sum:
    print("Yes")
    print(f"Sum = {even_sum}")
else:
    print("No")
    result = even_sum - odd_sum
    print(f"Diff = {abs(result)}")



