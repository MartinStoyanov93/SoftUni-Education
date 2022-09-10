my_dict = {}

text = input()
while not text == "statistics":
    product, quantity = text.split(": ")

    if product not in my_dict:
        my_dict[product] = 0
    my_dict[product] += int(quantity)

    text = input()

print("Products in stock:")
for product, quantity in my_dict.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(my_dict)}")
print(f"Total Quantity: {sum(my_dict.values())}")

