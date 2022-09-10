import re

total_cost = 0
products = []
pattern = r"\>{2}(?P<product>[A-Z][A-Za-z]+)\<{2}(?P<price>[0-9]+[\.0-9]*)\!(?P<quantity>[0-9]+)\b"

data = input()
while not data == "Purchase":
    matches = re.finditer(pattern, data)
    for match in matches:
        products.append(match.group('product'))
        price = float(match.group('price'))
        quantity = int(match.group('quantity'))
        total_cost += price * quantity

    data = input()

print("Bought furniture:")
for product in products:
    print(f"{product}")
print(f"Total money spend: {total_cost:.2f}")