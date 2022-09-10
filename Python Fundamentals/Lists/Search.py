# You will receive a number n and a word. On the next n lines you will be given some strings.
# You should add them in a list and print them.
# After that you should filter out only the strings that include the given word and print that list too

number = int(input())
word = input()

list = []
special_list = []

for n in range(number):
    string = input()
    list.append(string)
    if word in string:
        special_list.append(string)

print(list)
print(special_list)