strawberries_price = float(input())
banana_kg = float(input())
oranges_kg = float(input())
raspberries_kg = float(input())
strawberries_kg = float(input())

raspberries_price = strawberries_price / 2
oranges_price = raspberries_price - (raspberries_price * 0.4)
banana_price = raspberries_price - (raspberries_price * 0.8)

raspberries_sum = raspberries_price * raspberries_kg
banana_sum = banana_kg * banana_price
orange_sum = oranges_kg * oranges_price
strawberries_sum = strawberries_kg * strawberries_price

total_sum = raspberries_sum + banana_sum + orange_sum + strawberries_sum
print(total_sum)

