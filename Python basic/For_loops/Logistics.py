n = int(input())  # Тонаж

total_tons = 0     # средна цена на тон
minibus_price = 0
truck_price = 0
train_price = 0
minubus = 0
truck = 0
train = 0

for i in range(n):
    tons = int(input())
    if tons <= 3:
        minibus_price += tons * 200
        minubus += tons
    elif 4 <= tons <= 11:
        truck_price += tons * 175
        truck += tons
    else:
        train_price += tons * 120
        train += tons

total_tons = minubus + truck + train
average_price = (minibus_price + train_price + truck_price) / total_tons
minibus_percent = (minubus / total_tons) * 100
truck_percent = (truck / total_tons) * 100
train_percent = (train / total_tons) * 100

print(f"{average_price:.2f}")
print(f"{minibus_percent:.2f}%")
print(f"{truck_percent:.2f}%")
print(f"{train_percent:.2f}%")