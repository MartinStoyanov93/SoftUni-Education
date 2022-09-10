countries = input().split(", ")
capitals = input().split(", ")

my_dict = dict(zip(countries, capitals))

for key in my_dict:
    print(f"{key} -> {my_dict[key]}")
