message = input()

text = input()
while not text == "Reveal":
    data = text.split(":|:")
    command = data[0]

    if command == "InsertSpace":
        index = int(data[1])
        for i in range(len(message)):
            if i == index:
                message = message[:index] + " " + message[index:]
        print(message)

    elif command == "Reverse":
        substring = data[1]
        reversed_word = ""
        if substring in message:
            for el in reversed(substring):
                reversed_word += el
            message = message.replace(substring, reversed_word)
            print(message)
        else:
            print("error")

    elif command == "ChangeAll":
        substring = data[1]
        replacement = data[2]
        if substring in message:
            message = message.replace(substring, replacement)

        print(message)

    text = input()

print(f"You have a new text message: {message}")