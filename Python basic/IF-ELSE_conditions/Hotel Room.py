month = input()
nights = int(input())

studio = ""
apartments = ""

if month == "May" or month == "October":
    if nights > 14:
        apartments = nights * 65 - ((nights * 65) * 0.1)
        studio = (nights * 50) - ((nights * 50) * 0.3)
        print(f"Apartment: {float(apartments):.2f} lv.")
        print(f"Studio: {float(studio):.2f} lv.")
    elif nights > 7:
        apartments = nights * 65
        studio = (nights * 50) - ((nights * 50) * 0.05)
        print(f"Aparment: {float(apartments):.2f} lv.")
        print(f"Studio: {float(studio):.2f} lv.")
    else:
        apartments = nights * 65
        studio = nights * 50
        print(f"Apartment: {float(apartments):.2f} lv.")
        print(f"Studio: {float(studio):.2f} lv.")
elif month == "June" or month == "September":
    if nights > 14:
        apartments = nights * 68.70 - ((nights * 68.70) * 0.1)
        studio = (nights * 75.20) - ((nights * 75.20) * 0.2)
        print(f"Apartment: {float(apartments):.2f} lv.")
        print(f"Studio: {float(studio):.2f} lv.")
    else:
        nights <= 14
        apartments = nights * 68.70
        studio = nights * 75.20
        print(f"Apartment: {float(apartments):.2f} lv.")
        print(f"Studio: {float(studio):.2f} lv.")
elif month == "July" or month == "August":
    if nights > 14:
        apartments = (nights * 77) - ((nights * 77) * 0.1)
        studio = nights * 76
        print(f"Apartment: {float(apartments):.2f} lv.")
        print(f"Studio: {float(studio):.2f} lv.")
    else:
        apartments = nights *77
        studio = nights * 76
        print(f"Apartment: {float(apartments):.2f} lv.")
        print(f"Studio: {float(studio):.2f} lv.")