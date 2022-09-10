def shopping_list(budget, **shop_list):
    result = []
    if budget < 100:
        return "You do not have enough budget."
    else:
        basket = 0
        for key, value in shop_list.items():
            name = key
            price = float(value[0])
            quantity = int(value[1])
            total_price = price * quantity

            if basket == 5:
                break

            if total_price > budget:
                continue

            budget -= total_price
            basket += 1
            result.append(f"You bought {name} for {total_price:.2f} leva.")

    return '\n'.join(str(x) for x in result)


# print(shopping_list(100, microwave=(70, 2), skirts=(15, 4), coffee=(1.50, 10)))

# print(shopping_list(20, jeans=(19.99, 1),))
#
print(shopping_list(104, cola=(1.20, 2), candies=(0.25, 15), bread=(1.80, 1), pie=(10.50, 5), tomatoes=(4.20, 1), milk=(2.50, 2), juice=(2, 3), eggs=(3, 1)))
