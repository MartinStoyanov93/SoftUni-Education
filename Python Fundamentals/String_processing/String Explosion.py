text = input()

total_strength = 0
result = ""

i = 0
while i <len(text):
    current_char = text[i]

    if not current_char == ">":
        result += current_char
    else:
        result += ">"
        total_strength += int(text[i + 1])

        while total_strength > 0:
            i += 1

            if i >= len(text):
                break

            current_char = text[i]
            if current_char == ">":
                result += ">"
                total_strength += int(text[i + 1])
            else:
                total_strength -= 1

    i += 1

print(result)





