projection = input()
rowls = int(input())
colunms = int(input())

income = 0
capacity = rowls * colunms

if projection == "Premiere":
    income = capacity * 12.00
    print(f"{income:.2f} leva")
elif projection == "Normal":
    income = capacity * 7.50
    print(f"{income:.2f} leva")
elif projection == "Discount":
    income = capacity * 5.00
    print(f"{income:.2f} leva")
