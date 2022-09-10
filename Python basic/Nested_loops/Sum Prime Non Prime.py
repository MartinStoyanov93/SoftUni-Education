tshirt_price = float(input())
target = float(input())

pants_price = tshirt_price * 0.75
socks_price = pants_price * 0.20
shoes_price = (tshirt_price + pants_price) * 2

sum = pants_price + shoes_price + socks_price + tshirt_price
discount = sum * 0.15
total_sum = sum - discount


if total_sum >= target:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_sum:.2f} lv.")
else:
    diff = target - total_sum
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {diff:.2f} lv. more. ")