string = input()

current_char = ""
end_char = ""

for char in string:
    if not char == current_char:
        current_char = char
        end_char += current_char

print(end_char)