journey_price = float(input())
puzzle = int(input())
dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())


puzzle_price = puzzle * 2.60
price_dolls = dolls * 3
price_teddy_bears = teddy_bears * 4.10
price_minions = minions * 8.20
price_trucks = trucks * 2

total_price = puzzle_price + price_dolls + price_minions + price_trucks + price_teddy_bears

toys_count = puzzle + dolls + teddy_bears + minions + trucks

if toys_count > 50:
    discount = total_price * 0.25
    total_price = total_price - discount
    rent = total_price * 0.1
    total_price -= rent
    if total_price > journey_price:
        money_left = total_price - journey_price
        print(f"Yes! {money_left:.2f} lv left.")
    else:
        money_needed = journey_price - total_price
        print(f"Not enough money! {money_needed:.2f} lv needed.")
else:
    rent = total_price * 0.1
    total_price -= rent
    if total_price > journey_price:
        money_left = total_price - journey_price
        print(f"Yes! {money_left:.2f} lv left.")
    else:
        money_needed = journey_price - total_price
        print(f"Not enough money! {money_needed:.2f} lv needed.")


