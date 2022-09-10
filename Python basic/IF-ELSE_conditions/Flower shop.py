import math


magnolias = int(input())
hyacinth = int(input())
roses = int(input())
cactus = int(input())
present = float(input())

magnolias_count = magnolias * 3.25
hyacinth_count = hyacinth * 4
roses_count = roses * 3.50
cactus_count = cactus * 8

Sum = magnolias_count + hyacinth_count + roses_count + cactus_count
Total_sum = Sum - Sum * 0.05

if Total_sum >= present:
    diff = Total_sum - present
    print(f"She is left with {math.floor(diff)} leva.")
else:
    diff = present - Total_sum
    print(f"She will have to borrow {math.ceil(diff)} leva.")
