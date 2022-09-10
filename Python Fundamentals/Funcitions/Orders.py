order = input()
quantity = int(input())


def order_calculator():
    total_price = None
    if order == "coffee":
        total_price = quantity * 1.50
    elif order == "water":
        total_price = quantity * 1.00
    elif order == "coke":
        total_price = quantity * 1.40
    elif order == "snack":
        total_price = quantity * 2.00

    return total_price


print(f"{order_calculator():.2f}")
