budget = float(input())
season = input()

vacation_type = ""
destination = ""

if season == "summer":
    if budget <= 100:
        vacation_type = "Camp"
        destination = "Bulgaria"
        money_used = budget * 0.3
        print(f"Somewhere in {destination}")
        print(f"{vacation_type} - {money_used:.2f}")
    elif budget <= 1000:
        vacation_type = "Camp"
        destination = "Balkans"
        money_used = budget * 0.4
        print(f"Somewhere in {destination}")
        print(f"{vacation_type} - {money_used:.2f}")
    elif budget > 1000:
        vacation_type = "Hotel"
        destination = "Europe"
        money_used = budget * 0.9
        print(f"Somewhere in {destination}")
        print(f"{vacation_type} - {money_used:.2f}")
elif season == "winter":
    if budget <= 100:
        vacation_type = "Hotel"
        destination = "Bulgaria"
        money_used = budget * 0.7
        print(f"Somewhere in {destination}")
        print(f"{vacation_type} - {money_used:.2f}")
    elif budget <= 1000:
        vacation_type = "Hotel"
        destination = "Balkans"
        money_used = budget * 0.8
        print(f"Somewhere in {destination}")
        print(f"{vacation_type} - {money_used:.2f}")
    elif budget > 1000:
        vacation_type = "Hotel"
        destination = "Europe"
        money_used = budget * 0.9
        print(f"Somewhere in {destination}")
        print(f"{vacation_type} - {money_used:.2f}")