budget = float(input())
participants = int(input())
clothes = float(input())

decor = budget * 0.1
clothes_sum = clothes * participants
if participants > 150:
    discount = clothes_sum * 0.1
    clothes_sum -= discount

total_film_sum = decor + clothes_sum

if total_film_sum < budget:
    money_left = budget - total_film_sum
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")
else:
    money_needed = total_film_sum - budget
    print("Not enough money!")
    print(f"Wingard needs {money_needed:.2f} leva more.")