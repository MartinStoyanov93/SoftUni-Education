data = input()
my_dict = {}

for char in data:
    if not char == " ":
        if char not in my_dict:
            my_dict[char] = 1
        else:
            my_dict[char] += 1
    else:
        pass

for key, value in my_dict.items():
    print(f"{key} -> {value}")
