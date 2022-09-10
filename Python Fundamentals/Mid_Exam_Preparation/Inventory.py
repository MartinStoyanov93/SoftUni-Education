item_collection = input().split(", ")

data = input()

while not data == "Craft!":
    command = data.split(" - ")

    if command[0] == "Collect":
        item = command[1]
        if item not in item_collection:
            item_collection.append(item)

    if command[0] == "Drop":
        item = command[1]
        if item in item_collection:
            index = item_collection.index(item)
            item_collection.pop(index)

    if command[0] == "Combine Items":
        combined_item = command[1].split(":")
        if combined_item[0] in item_collection:
            index = item_collection.index(combined_item[0])
            item_collection.insert(index + 1, combined_item[1])

    if command[0] == "Renew":
        item = command[1]
        if item in item_collection:
            index = item_collection.index(item)
            item_collection.pop(index)
            item_collection.append(item)

    data = input()

print(", ".join(item_collection))