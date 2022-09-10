dungeon_room = input().split("|")
health = 100
bitcoin = 0
counter = 0

for room in range(len(dungeon_room)):
    counter += 1
    r = dungeon_room[room].split()
    command = r[0]
    number = int(r[1])

    if command == "potion":
        if health + number > 100:
            amount = 100 - health
            health = 100
            print(f"You healed for {amount} hp.")
            print(f"Current health: {health} hp.")
        else:
            health += number
            print(f"You healed for {number} hp.")
            print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoin += number
        print(f"You found {number} bitcoins.")

    else:
        health -= number
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {counter}")
            break

if health > 0:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoin}")
    print(f"Health: {health}")



