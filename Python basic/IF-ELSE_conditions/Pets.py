import math


days = int(input())
food = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input()) / 1000

dog_food = days * dog_food_per_day
cat_food = days * cat_food_per_day
turtle_food = days * turtle_food_per_day
total_food = dog_food + cat_food + turtle_food

if total_food <= food:
    food_left = food - total_food
    print(f"{math.floor(food_left)} kilos of food left.")
else:
    food_needed = total_food - food
    print(f"{math.ceil(food_needed)} more kilos of food are needed.")