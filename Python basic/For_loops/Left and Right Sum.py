n = int(input())

sum1 = 0
sum2 = 0
for i in range(n):
    n1 = int(input())
    sum1 += n1

for i in range(n):
    n2 = int(input())
    sum2 += n2

result = 0

if sum1 != sum2:
    result = sum1 - sum2
    print(f"No, diff = {abs(result)}")
else:
    result = sum1
    print(f"Yes, sum = {result}")


