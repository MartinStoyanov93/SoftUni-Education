targets = [int(el) for el in input().split()]
result = []
data = input()
while not data == "End":
    command = data.split()

    if command[0] == "Shoot":
        index = int(command[1])
        power = int(command[2])
        if index in range(len(targets)):
            targets[index] -= power
            if targets[index] <= 0:
                targets.pop(index)

    elif command[0] == "Add":
        index = int(command[1])
        value = int(command[2])
        if index <= len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif command[0] == "Strike":
        index = int(command[1])
        radius = int(command[2])
        left_index = index - radius
        right_index = index + radius
        if index in range(len(targets)) and left_index in range(len(targets)) and right_index in range(len(targets)):
            left_unstriketed = targets[:left_index]
            right_unstriketed = targets[right_index + 1:]
            targets = left_unstriketed + right_unstriketed
        else:
            print("Strike missed!")

    data = input()

print("|".join([str(el) for el in targets]))