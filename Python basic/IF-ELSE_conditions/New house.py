flower = input()
number = int(input())
budget = int(input())

price = 0
discount = 0

if flower == "Roses":
    price = 5
    if number > 80:
        price -= price * 0.1

elif flower == "Dahlias":
    price = 3.80
    if number > 90:
        price -= price * 0.15

elif flower == "Tulips":
    price = 2.80
    if number > 80:
        price -= price * 0.15

elif flower == "Narcissus":
    price = 3
    if number < 120:
        price += price * 0.15

elif flower == "Gladiolus":
    price = 02.50
    if number < 80:
        price += price * 0.2

money_needed = number * price
diff = abs(budget - money_needed)
if budget >= money_needed:
    print(f"Hey, you have a great garden with {number} {flower} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")

