import math

budget = float(input())
students = int(input())
flour= float(input())
egg = float(input()) * 10
apron = float(input())
total_price = 0
free_flour = 0


for i in range(1, students + 1):
    if i % 5 == 0:
        free_flour += flour

apron_price = apron * (students + math.ceil(students * 0.2))
egg_price = students * egg
flour_price = (flour * students) - free_flour

total_price = apron_price + egg_price + flour_price

if total_price <= budget:
    print(f"Items purchased for {total_price:.2f}$.")
else:
    needed_money = abs(budget - total_price)
    print(f"{needed_money:.2f}$ more needed.")