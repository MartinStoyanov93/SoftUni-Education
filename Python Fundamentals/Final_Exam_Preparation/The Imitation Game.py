encrypted_text = input()

data = input()
while not data == "Decode":
    string = data.split("|")
    command = string[0]

    if command == "Move":
        num_of_letters = int(string[1])
        char_to_move = ""
        for char in range(0, num_of_letters):
            char_to_move += encrypted_text[char]
        encrypted_text = encrypted_text.replace(char_to_move, "")
        encrypted_text = encrypted_text + char_to_move

    elif command == "Insert":
        index = int(string[1])
        value = string[2]
        current_string = ""
        start_string = encrypted_text[:index]
        end_string = encrypted_text[index:]
        encrypted_text = start_string + value + end_string

    elif command == "ChangeAll":
        substring = string[1]
        replacement = string[2]
        if substring in encrypted_text:
            encrypted_text = encrypted_text.replace(substring,replacement)


    data = input()

print(f"The decrypted message is: {encrypted_text}")


