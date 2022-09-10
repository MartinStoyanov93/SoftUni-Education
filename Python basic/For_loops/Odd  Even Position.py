import sys
number = int(input())

odd_max = -sys.maxsize
odd_min = sys.maxsize
odd_sum = 0
even_max = -sys.maxsize
even_min = sys.maxsize
even_sum = 0

for i in range(1, number + 1):
    num = float(input())
    if i % 2 == 0:
        if even_max < num:
            even_max = num
        if even_min > num:
            even_min = num
        even_sum += num
    else:
        if odd_max < num:
            odd_max = num
        if odd_min > num:
            odd_min = num
        odd_sum += num

print(f"OddSum={odd_sum:.2f},")
if odd_min != sys.maxsize:
    print(f"OddMin={odd_min:.2f},")
else:
    print("OddMin=No,")

if odd_max != -sys.maxsize:
    print(f"OddMax={odd_max:.2f},")
else:
    print("OddMax=No,")
print(f"EvenSum={even_sum:.2f},")
if even_min != sys.maxsize:
    print(f"EvenMin={even_min:.2f},")
else:
    print("EvenMin=No,")

if even_max != -sys.maxsize:
    print(f"EvenMax={even_max:.2f}")
else:
    print("EvenMax=No")