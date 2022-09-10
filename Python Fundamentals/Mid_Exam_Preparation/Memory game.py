def is_invalid(ind_1, ind_2):
    if ind_1 == ind_2:
        return True
    elif ind_1 < 0 or ind_2 < 0:
        return True
    elif ind_1 and ind_2 > len(elements):
        return True
    return False


elements = input().split()
moves = 0
error = f"-{moves}a"

command = input()
while not command == "end" and elements:
    index_1, index_2 = command.split()
    index_1 = int(index_1)
    index_2 = int(index_2)

    moves += 1

    if elements[index_1] == elements[index_2]:
        el_1 = elements[index_1]
        el_2 = elements[index_2]
        elements.remove(el_1)
        elements.remove(el_2)
        print(f"Congrats! You have found matching elements - {el_1}!")

    elif is_invalid(index_1, index_2):
        middle = len(elements) // 2
        elements.insert(middle, f"-{str(moves)}a")
        elements.insert(middle, f"-{str(moves)}a")
        print("Invalid input! Adding additional elements to the board")

    else:
        print("Try again!")

    command = input()

if not elements:
    print(f"You have won in {moves} turns!")
else:
    print("Sorry you lose :(")
    print(" ".join(elements))
