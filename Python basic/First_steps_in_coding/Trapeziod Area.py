vegetable_price = float(input())
fruit_price = float(input())
veg_kg = int(input())
fruit_kg = int(input())

total_veg_price = vegetable_price * veg_kg
total_fruit_price = fruit_price  * fruit_kg

income = (total_fruit_price + total_veg_price) / 1.94

print(f"{income:.2f}")