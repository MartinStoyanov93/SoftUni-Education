original_deck = input().split(":")
new_deck = []

data = input()

while not data == "Ready":
    card = data.split()
    command = card[0]
    card_name = card[1]

    if command == "Add":
        if card_name in original_deck:
            new_deck.append(card_name)
        else:
            print("Card not found.")

    if command == "Insert":
        index = int(card[2])
        if index in range(len(original_deck)) and card_name in original_deck:
            new_deck.insert(index, card_name)
        else:
            print("Error!")

    if command == "Remove":
        if card_name in new_deck:
            new_deck.remove(card_name)
        else:
            print("Card not found.")

    if command == "Swap":
        card_name_2 = card[2]
        index_1 = new_deck.index(card_name)
        index_2 = new_deck.index(card_name_2)
        new_deck[index_1], new_deck[index_2] = new_deck[index_2], new_deck[index_1]

    if data == "Shuffle deck":
        new_deck.reverse()

    data = input()

if data == "Ready":
    print(" ".join(new_deck))