strings = input()

while not strings == "end":

    reversed_word = ""
    for el in reversed(strings):
        reversed_word += el
    print(f"{strings} = {reversed_word}")

    strings = input()

