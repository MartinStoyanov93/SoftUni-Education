season = input()
km_per_month = float(input())

salary = 0

if km_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        salary = (km_per_month * 0.75) * 4
    elif season == "Summer":
        salary = (km_per_month * 0.9) * 4
    elif season == "Winter":
        salary = (km_per_month * 1.05) * 4
elif 5000 < km_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        salary = (km_per_month * 0.95) * 4
    elif season == "Summer":
        salary = (km_per_month * 1.10) * 4
    elif season == "Winter":
        salary = (km_per_month * 1.25) * 4
elif 10000 < km_per_month <= 20000:
    if season == "Spring" or season == "Autumn" or season == "Summer" or season == "Winter":
        salary = (km_per_month * 1.45) * 4

tax = salary * 0.1
salary = salary - tax
print(f"{salary:.2f}")