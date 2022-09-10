string = input()
digits = ""
alpha = ""
symbols = ""
for char in string:
    if char.isdigit():
        digits += char
    elif char.isalpha():
        alpha += char
    else:
        symbols += char

print(digits)
print(alpha)
print(symbols)
