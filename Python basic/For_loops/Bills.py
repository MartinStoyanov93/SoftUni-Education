n = int(input()) # months

electricity = 0
water = 0
internet = 0
other = 0
average = 0

for i in range(n):
    bills = float(input()) #for electricity
    electricity += bills
    water += 20
    internet += 15
    other = ((electricity + water + internet) * 0.20) + (electricity + water + internet)

average = (electricity + water + internet +other) / n

print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {other:.2f} lv")
print(f"Average: {average:.2f} lv")
