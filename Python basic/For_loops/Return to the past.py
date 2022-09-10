money = float(input())
year = int(input())

age = 18
money_spent = 0

for i in range(1801, year + 1):
    if i % 2 == 0:
        money_spent += 12000
        age += 1
    else:
        money_spent += 12000 + (age * 50)
        age += 1

if money_spent < money:
    money_left = money - money_spent
    print(f"Yes! He will live a carefree life and will have {money_left:.2f} dollars left.")
else:
    money_needed = money_spent - money
    print(f"He will need {money_needed:.2f} dollars to survive.")