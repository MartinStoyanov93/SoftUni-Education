total_price_produt = {}
price_menu = {}
qty_menu = {}


data = input()
while not data == "buy":
    product, price, quantity = data.split()

    if product not in total_price_produt:
        total_price_produt[product] = 0
        price_menu[product] = float(price)
        qty_menu[product] = int(quantity)
    else:
        qty_menu[product] += int(quantity)
        if not price == price_menu[product]:
            price_menu[product] = float(price)

    data = input()

for product in total_price_produt:
    total_price_produt[product] = price_menu[product] * qty_menu[product]

for key, value in total_price_produt.items():
    print(f"{key} -> {value:.2f}")


#  WITH FUNCTION

def order(total_price :dict, price :dict, quantity :dict, cena, qty, product):

    if product not in total_price_produt:
        total_price[product] = 0
        price[product] = float(cena)
        quantity[product] = int(qty)
    else:
        quantity[product] += int(qty)
        if not price == price[product]:
            price[product] = float(cena)


total_price_produt = {}
price_menu = {}
qty_menu = {}

data = input()
while not data == "buy":
    product, price, quantity = data.split()

    order(total_price_produt, price_menu, qty_menu, price, quantity, product)

    data = input()

for product in total_price_produt:
    total_price_produt[product] = price_menu[product] * qty_menu[product]

for key, value in total_price_produt.items():
    print(f"{key} -> {value:.2f}")