fuel_type = input()
fuel_count = float(input())
card_club = input()


if fuel_type == "Gasoline":
    Sum = fuel_count * 2.22
    if card_club == "Yes":
        card_discount = fuel_count * 0.18
        Sum = Sum - card_discount
    if 20 < fuel_count <= 25:
        discount = Sum * 0.08
        Sum = Sum - discount
    elif fuel_count > 25:
        discount = Sum * 0.1
        Sum = Sum - discount
    print(f"{Sum:.2f} lv.")

elif fuel_type == "Diesel":
    Sum = fuel_count * 2.33
    if card_club == "Yes":
        card_discount = fuel_count * 0.12
        Sum = Sum - card_discount
    if 20 < fuel_count <= 25:
        discount = Sum * 0.08
        Sum = Sum - discount
    elif fuel_count > 25:
        discount = Sum * 0.1
        Sum = Sum - discount
    print(f"{Sum:.2f} lv.")

elif fuel_type == "Gas":
    Sum = fuel_count * 0.93
    if card_club == "Yes":
        card_discount = fuel_count * 0.08
        Sum = Sum - card_discount
    if 20 < fuel_count <= 25:
        discount = Sum * 0.08
        Sum = Sum - discount
    elif fuel_count > 25:
        discount = Sum * 0.1
        Sum = Sum - discount
    print(f"{Sum:.2f} lv.")