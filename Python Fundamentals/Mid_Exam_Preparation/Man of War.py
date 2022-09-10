pirate_status = [int(num) for num in input().split(">")]
warship_status = [int(num) for num in input().split(">")]
max_health = int(input())
is_sunk = False

command = input()

while not command == "Retire":
    data = command.split()

    if data[0] == "Fire":
        index = int(data[1])
        damage = int(data[2])
        if 0 <= index < len(warship_status):
            warship_status[index] -= damage
            if warship_status[index] <= 0:
                print("You won! The enemy ship has sunken.")
                is_sunk = True
                break

    elif data[0] == "Defend":
        start_index = int(data[1])
        end_index = int(data[2])
        damage = int(data[3])
        if 0 <= start_index < len(pirate_status) and 0 <= end_index < len(pirate_status):
            for i in range(start_index, end_index + 1):
                pirate_status[i] -= damage
                if pirate_status[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    is_sunk = True
                    break

    elif data[0] == "Repair":
        index = int(data[1])
        health = int(data[2])
        if 0 <= index < len(pirate_status):
            if pirate_status[index] + health > max_health:
                pirate_status[index] = max_health
            else:
                pirate_status[index] += health

    elif data[0] == "Status":
        min_health = max_health * 0.2
        counter = 0
        for ship in pirate_status:
            if ship < min_health:
                counter += 1
        print(f"{counter} sections need repair.")

    command = input()

if not is_sunk:
    print(f"Pirate ship status: {sum(pirate_status)}")
    print(f"Warship status: {sum(warship_status)}")

