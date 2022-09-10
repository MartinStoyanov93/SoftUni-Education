number = int(input())
my_dict = {}

while number >= 1:
    word = input()
    synonym = input()
    number -= 1

    if word not in my_dict:
        my_dict[word] = []
        my_dict[word].append(synonym)
    else:
        my_dict[word].append(synonym)

for word in my_dict:
    print(f"{word} - {', '.join(my_dict[word])}")

