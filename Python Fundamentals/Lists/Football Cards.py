Team_A = 11
Team_B = 11
A_list = []
B_list = []

string_of_red_cards = input()
list = string_of_red_cards.split(" ")

for el in list:
    if "A" in el:
        if el in A_list:
            pass
        else:
            A_list.append(el)
            Team_A -= 1
    elif "B" in el:
        if el in B_list:
            pass
        else:
            B_list.append(el)
            Team_B -= 1

    if Team_B < 7 or Team_A < 7:
        break

if Team_A < 7 or Team_B < 7:
    print(f"Team A - {Team_A}; Team B - {Team_B}")
    print("Game was terminated")
else:
    print(f"Team A - {Team_A}; Team B - {Team_B}")