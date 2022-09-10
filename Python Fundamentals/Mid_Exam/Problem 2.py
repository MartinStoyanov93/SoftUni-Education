def is_valid(ind, friends):
    if ind in range(len(friends)):
        return True
    return False


friend_list = input().split(", ")
blacklist_count = 0
lost_count = 0

data = input()
while not data == "Report":
    text = data.split()
    command = text[0]

    if command == "Blacklist":
        name = text[1]
        new_name = "Blacklisted"
        if name in friend_list:
            index = friend_list.index(name)
            friend_list[index] = new_name
            print(f"{name} was blacklisted.")
            blacklist_count += 1
        else:
            print(f"{name} was not found.")

    if command == "Error":
        index = int(text[1])
        name = friend_list[index]
        new_name = "Lost"
        if is_valid(index, friend_list) and not friend_list[index] == "Lost" and not friend_list[index] == "Blacklisted":
            friend_list[index] = new_name
            print(f"{name} was lost due to an error.")
            lost_count += 1

    if command == "Change":
        index = int(text[1])
        new_name = text[2]
        if is_valid(index, friend_list):
            current_name = friend_list[index]
            friend_list[index] = new_name
            print(f"{current_name} changed his username to {new_name}.")

    data = input()

if data == "Report":
    print(f"Blacklisted names: {blacklist_count}")
    print(f"Lost names: {lost_count}")
    print(" ".join(friend_list))

