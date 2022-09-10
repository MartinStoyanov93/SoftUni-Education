my_dict = {}

text = input()
while not text == "stop":
    data = text
    quantity = int(input())

    if data not in my_dict:
        my_dict[data] = 0
        my_dict[data] += quantity
    else:
        my_dict[data] += quantity

    text = input()


for key in my_dict:
    print(f"{key} -> {my_dict[key]}")