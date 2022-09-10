budget = int(input())
season = input()
count_fisherman = int(input())

rent = 0

if season == "Spring":
    rent = 3000
elif season == "Summer" or season == "Autumn":
    rent = 4200
elif season == "Winter":
    rent = 2600

if count_fisherman <= 6:
    rent = rent - (rent * 0.1)
elif count_fisherman <= 11:
    rent = rent - (rent * 0.15)
elif count_fisherman >= 12:
    rent = rent - (rent * 0.25)

if count_fisherman % 2 == 0 and season != "Autumn":
    rent -= rent * 0.05

diff = abs(budget - rent)
if budget < rent:
        print(f"Not enough money! You need {diff:.2f} leva.")
else:
        print(f"Yes! You have {diff:.2f} leva left.")
