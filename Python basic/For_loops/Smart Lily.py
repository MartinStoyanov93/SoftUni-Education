age = int(input())
price = float(input())
toy_price = int(input())

saved_money = 0

for year in range(1, age + 1):
    if year % 2 == 0:
        saved_money += (year * 10 / 2) - 1
    else:
        saved_money += toy_price

diff = abs(saved_money - price)
if saved_money >= price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
