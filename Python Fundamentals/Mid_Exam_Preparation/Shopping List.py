shopping_list = input().split("!")

text = input()
while not text == "Go Shopping!":
    data = text.split()
    command = data[0]
    item = data[1]

    if command == "Urgent":
        if item not in shopping_list:
            shopping_list.insert(0, item)

    elif command == "Unnecessary":
        if item in shopping_list:
            shopping_list.remove(item)

    elif command == "Correct":
        item_2 = data[2]
        if item in shopping_list:
            index = shopping_list.index(item)
            shopping_list[index] = item_2

    elif command == "Rearrange":
        if item in shopping_list:
            index = shopping_list.index(item)
            shopping_list.pop(index)
            shopping_list.append(item)

    text = input()

print(", ".join(shopping_list))


