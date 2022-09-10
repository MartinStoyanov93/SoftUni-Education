text = input()
encrypted_code = ""

for i in text:
    current_position = ord(i) + 3
    encrypted_code += chr(current_position)

print(encrypted_code)


