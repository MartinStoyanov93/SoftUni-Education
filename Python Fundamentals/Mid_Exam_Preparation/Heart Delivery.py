neighborhood = [int(num) for num in input().split("@")]
count = 0
position = 0

data = input()
while not data == "Love!":
    command = data.split()
    length = int(command[1])
    position += length

    if position >= len(neighborhood):
        position = 0

    if neighborhood[position] == 0:
        print(f"Place {position} already had Valentine's day.")

    else:
        neighborhood[position] -= 2
        if neighborhood[position] == 0:
            print(f"Place {position} has Valentine's day.")

    data = input()


print(f"Cupid's last position was {position}.")

for n in neighborhood:
    if not n == 0:
        count += 1

if count == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {count} places.")
