my_dict = {}

data = input()
while not data == "End":
    company_name, id = data.split(" -> ")

    if company_name not in my_dict:
        my_dict[company_name] = [id]
    else:
        if id in my_dict[company_name]:
            pass
        else:
            my_dict[company_name].append(id)

    data = input()

sorted_dict = sorted(my_dict.items(), key=lambda x: x[0])
for company, id in sorted_dict:
    print(f"{company}")
    for v in id:
        print("--", v)
