from collections import deque

list_of_materials = [int(x) for x in input().split()]
genie_magic = deque([int(x) for x in input().split()])

crafted_presents = {
    'Gemstone': 0,
    'Porcelain Sculpture': 0,
    'Gold': 0,
    'Diamond Jewellery': 0
}

while True:
    if not list_of_materials or not genie_magic:
        break
    material = list_of_materials.pop()
    magic = genie_magic.popleft()
    sum = material + magic

    if sum < 100:
        if sum % 2 == 0:
            sum = (material * 2) + (magic * 3)
        else:
            sum = sum * 2

    elif sum > 499:
        sum = sum / 2

    if 100 <= sum <= 199:
        crafted_presents['Gemstone'] += 1
    elif 200 <= sum <= 299:
        crafted_presents['Porcelain Sculpture'] += 1
    elif 300 <= sum <= 399:
        crafted_presents['Gold'] += 1
    elif 400 <= sum <= 499:
        crafted_presents['Diamond Jewellery'] += 1

if crafted_presents['Gemstone'] > 0 and crafted_presents['Porcelain Sculpture'] > 0 or \
        crafted_presents['Gold'] > 0 and crafted_presents['Diamond Jewellery'] > 0:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if list_of_materials:
    print(f"Materials left: {', '.join(map(str, list_of_materials))}")
if genie_magic:
    print(f"Magic left: {', '.join(map(str, genie_magic))}")


for key, value in sorted(crafted_presents.items(), key=lambda x: x[0]):
    if crafted_presents[key] > 0:
        print(f"{key}: {value}")

