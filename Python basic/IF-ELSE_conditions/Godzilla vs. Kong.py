budget = float(input())
actors = int(input())
price_per_cloath = float(input())

decor_sum = budget * 0.1
clothing = price_per_cloath * actors

if actors > 150:
    discount = clothing * 0.1
    clothing = clothing - discount
    total_budget = clothing + decor_sum
else:
    total_budget = clothing + decor_sum

if budget > total_budget:
    money_left = budget - total_budget
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")
else:
    money_needed = total_budget - budget
    print("Not enough money!")
    print(f"Wingard needs {money_needed:.2f} leva more.")

