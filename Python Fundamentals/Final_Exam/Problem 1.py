string = input()

data = input()
while not data == "Done":
    command = data.split()

    if command[0] == "Change":
        char = command[1]
        replace_char = command[2]
        if char in string:
            string = string.replace(char, replace_char)
        print(string)

    elif command[0] == "Includes":
        other_string = command[1]
        if other_string in string:
            print("True")
        else:
            print("False")

    elif command[0] == "End":
        other_string = command[1]
        if string.endswith(other_string):
            print("True")
        else:
            print("False")

    elif command[0] == "Uppercase":
        string = string.upper()
        print(string)

    elif command[0] == "FindIndex":
        char = command[1]
        index = string.find(char)
        print(index)

    elif command[0] == "Cut":
        current_string = ""
        start_index = int(command[1])
        length = int(command[2])
        for el in range(len(string)):
            if el > (start_index - 1) and length >= 1:
                length -= 1
                letter = string[el]
                current_string += letter
        string = current_string
        print(string)

    data = input()