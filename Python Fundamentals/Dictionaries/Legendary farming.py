my_dict = {'shards': 0, 'fragments': 0, 'motes': 0}
junk = {}
item_obtained = ''

while item_obtained == '':
    materials = input().split()

    for el in range(0, len(materials), 2):
        element = materials[el + 1].lower()
        quantity = int(materials[el])

        if element == "shards" or element == "fragments" or element == "motes":
            my_dict[element] += quantity
        else:
            if element in junk:
                junk[element] += quantity
            else:
                junk[element] = quantity

        if my_dict["shards"] >= 250:
            item_obtained = "Shadowmourne"
            my_dict["shards"] -= 250
            break
        elif my_dict["fragments"] >= 250:
            item_obtained = "Valanyr"
            my_dict["fragments"] -= 250
            break
        elif my_dict["motes"] >= 250:
            item_obtained = "Dragonwrath"
            my_dict["motes"] -= 250
            break

print(f"{item_obtained} obtained!")
for key, value in sorted(my_dict.items(), key=lambda x: (-x[1], x[0])):
    print(f"{key}: {value}")

sorted_junk = sorted(junk.items(), key=lambda x: x[0])
for product, quantity in sorted_junk:
    print(f"{product}: {quantity}")
