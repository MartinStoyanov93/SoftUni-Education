chrysanthemums_number = int(input())
roses_number = int(input())
tulip_number = int(input())
season = input()
Holiday = input()

chrysanthemums_sum = 0
roses_sum = 0
tulip_sum = 0
price_flower = 0
flower_count = 0

flower_count = chrysanthemums_number + roses_number + tulip_number

if season == "Spring" or season == "Summer":
    chrysanthemums_sum = chrysanthemums_number * 2
    roses_sum = roses_number * 4.10
    tulip_sum = tulip_number * 2.50
elif season == "Autumn" or season == "Winter":
    chrysanthemums_sum = chrysanthemums_number * 3.75
    roses_sum = roses_number * 4.50
    tulip_sum = tulip_number * 4.15

price_flower = chrysanthemums_sum + roses_sum + tulip_sum

if Holiday == "Y":
    price_flower = price_flower + (price_flower * 0.15)

if tulip_number > 7 and season == "Spring":
    price_flower = price_flower - (price_flower * 0.05)

if roses_number >= 10 and season == "Winter":
    price_flower = price_flower - (price_flower * 0.1)

if flower_count >= 20:
    price_flower = price_flower - (price_flower * 0.2)

price_flower = price_flower + 2 # За аранжиране на бугет
print(f"{price_flower:.2f}")