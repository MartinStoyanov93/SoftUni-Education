Budget = float(input())
Season = input() # Summer or Winter

Class = ""
car_type = ""
car_price = 0

if Budget <= 100:
    Class = "Economy class"
    if Season == "Summer":
        car_type = "Cabrio"
        car_price = Budget * 0.35
    elif Season == "Winter":
        car_type = "Jeep"
        car_price = Budget * 0.65
elif 100 < Budget <= 500:
    Class = "Compact class"
    if Season == "Summer":
        car_type = "Cabrio"
        car_price = Budget * 0.45
    elif Season == "Winter":
        car_type = "Jeep"
        car_price = Budget * 0.8
else:
    Class = "Luxury class"
    if Season == "Summer" or "Winter":
        car_type = "Jeep"
        car_price = Budget * 0.9

print(f"{Class}")
print(f"{car_type} - {car_price:.2f}")