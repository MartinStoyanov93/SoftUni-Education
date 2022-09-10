km = int(input())
time_of_day = input()

if km < 20:
    if time_of_day == "day":
        price = 0.70 + km * 0.79
    elif time_of_day == "night":
        price = 0.70 + km * 0.90
elif km < 100:
    if time_of_day == "day" or "night":
        price = km * 0.09
else:
    if time_of_day == "day" or "night":
        price = km * 0.06
print(f"{price:.2f}")
