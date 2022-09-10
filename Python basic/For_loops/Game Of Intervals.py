n = int(input())  #ход

From_0_to_9 = 0
From_10_to_19 = 0
From_20_to_29 = 0
From_30_to_39 = 0
From_40_to_50 = 0
Invalid_number = 0
Result = 0

for i in range(n):
    number = int(input())
    if 0 <= number <= 9:
        Result += number * 0.20
        From_0_to_9 += 1
    elif 10 <= number <= 19:
        Result += number * 0.30
        From_10_to_19 += 1
    elif 20 <= number <= 29:
        Result += number * 0.40
        From_20_to_29 += 1
    elif 30 <= number <= 39:
        Result += 50
        From_30_to_39 += 1
    elif 40 <= number <= 50:
        Result += 100
        From_40_to_50 += 1

    if number < 0 or number > 50:
        Invalid_number += 1
        Result = Result / 2

Percent1 = (From_0_to_9 / n) * 100
Percent2 = (From_10_to_19 / n) * 100
Percent3 = (From_20_to_29 / n) * 100
Percent4 = (From_30_to_39 / n) * 100
Percent5 = (From_40_to_50 / n) * 100
Percent6 = (Invalid_number / n) * 100

print(f"{Result:.2f}")
print(f"From 0 to 9: {Percent1:.2f}%")
print(f"From 10 to 19: {Percent2:.2f}%")
print(f"From 20 to 29: {Percent3:.2f}%")
print(f"From 30 to 39: {Percent4:.2f}%")
print(f"From 40 to 50: {Percent5:.2f}%")
print(f"Invalid numbers: {Percent6:.2f}%")



