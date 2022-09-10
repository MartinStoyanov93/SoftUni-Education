stock = input().split()

my_dict = {}

for el in range(0, len(stock), 2):
    key = stock[el]
    value = stock[el + 1]
    my_dict[key] = int(value)

search_in_stock = input().split()

for _ in search_in_stock:
    if _ in my_dict:
        print(f"We have {my_dict[_]} of {_} left")
    else:
        print(f"Sorry, we don't have {_}")


