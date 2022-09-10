import math

harvest_area = int(input())
grape_per_square = float(input())
wine_expected = int(input())
workers = int(input())

total_grape_needed = harvest_area * grape_per_square
wine = (total_grape_needed * 0.4) / 2.5

if wine > wine_expected:
    wine_left = wine - wine_expected
    wine_per_worker = wine_left / workers
    print(F"Good harvest this year! Total wine: {math.floor(wine)} liters.")
    print(f"{math.ceil(wine_left)} liters left -> {math.ceil(wine_per_worker)} liters per person.")
else:
    wine_needed = wine_expected - wine
    print(f"It will be a tough winter! More {math.floor(wine_needed)} liters wine needed.")