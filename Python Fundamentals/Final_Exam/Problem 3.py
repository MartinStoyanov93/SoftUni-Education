my_dict = {}

store_data = input()
while store_data:
    word_definition = store_data.split(" | ")

    for element in word_definition:
        list_of_words = element.split(": ")
        word = list_of_words[0]
        definition = list_of_words[1]
        if word not in my_dict:
            my_dict[word] = [definition]
        else:
            my_dict[word].append(definition)

    break

test_words = input().split(" | ")
command = input()

if command == "Test":
    for word in test_words:
        if word in my_dict:
            print(f"{word}:")
            for element in sorted(my_dict[word], key=lambda x: len([x])):
                print(f"-{element}")

elif command == "Hand Over":
    for key, value in sorted(my_dict.items(), key=lambda x: x[0]):
        print(key, end=" ")