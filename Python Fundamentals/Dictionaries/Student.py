my_dict = {}

data = input()
while ":" in data:
    name, id, course = data.split(":")

    if course not in my_dict:
        my_dict[course] = {}
        my_dict[course][name] = id
    else:
        my_dict[course][name] = id

    data = input()


course = " ".join(data.split("_"))
for key, value in my_dict.items():
    if course == key:
        for name, id in value.items():
            print(f"{name} - {id}")
