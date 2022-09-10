# with list comprehension
string = input()
list_of_vowels = ['a', 'o', 'u', 'e', 'i']
print("".join([char for char in string if char.lower() not in list_of_vowels]))


# ---- with for cycle

# output = []
# for char in string:
#     if char in list_of_vowels:
#         pass
#     else:
#         output += char
#
# print(output)
# ------------

