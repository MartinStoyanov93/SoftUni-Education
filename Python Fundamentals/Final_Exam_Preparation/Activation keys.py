key_activation = input()

string = input()
while not string == "Generate":
    command = string.split(">>>")

    if command[0] == "Contains":
        substring = command[1]
        if substring in key_activation:
            print(f"{key_activation} contains {substring}")
        else:
            print("Substring not found!")

    elif command[0] == "Flip":
        type_of_letter = command[1]
        start_index = int(command[2])
        end_index = int(command[3])

        start_part = key_activation[:start_index]
        flip_part = key_activation[start_index:end_index]
        end_part = key_activation[end_index:]

        if type_of_letter == "Lower":
            flip_part = flip_part.lower()
        elif type_of_letter == "Upper":
            flip_part = flip_part.upper()
        key_activation = start_part + flip_part + end_part
        print(key_activation)

    elif command[0] == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        # for char in range(start_index, end_index):
        key_activation = key_activation[:start_index] + key_activation[end_index:]
        print(key_activation)

    string = input()

print(f"Your activation key is: {key_activation}")