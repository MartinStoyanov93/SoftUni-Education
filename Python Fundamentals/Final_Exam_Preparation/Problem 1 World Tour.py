string_to_manipulate = input()

text = input()
while not text == "Travel":
    command = text.split(":")

    if command[0] == "Add Stop":
        index = int(command[1])
        string = command[2]
        if 0 <= index < len(string_to_manipulate):
            string_to_manipulate = string_to_manipulate[:index] + f'{string}' + string_to_manipulate[index:]

    elif command[0] == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index < len(string_to_manipulate) and 0 <= end_index < len(string_to_manipulate):
            string_to_manipulate = string_to_manipulate[:start_index] + string_to_manipulate[end_index + 1:]

    elif command[0] == "Switch":
        old_sting = command[1]
        new_sting = command[2]
        if old_sting in string_to_manipulate:
            string_to_manipulate = string_to_manipulate.replace(old_sting, new_sting)
    print(string_to_manipulate)

    text = input()

print(f"Ready for world tour! Planned stops: {string_to_manipulate}")
