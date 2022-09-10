initial_energy = int(input())
battles_won = 0

command = input()
while not command == "End of battle":
    distance = int(command)

    if initial_energy >= distance:
        initial_energy -= distance
        battles_won += 1
    else:
        print(f"Not enough energy! Game ends with {battles_won} won battles and {initial_energy} energy")
        break

    if battles_won % 3 == 0:
        initial_energy += battles_won

    command = input()

if command == "End of battle":
    print(f"Won battles: {battles_won}. Energy left: {initial_energy}")