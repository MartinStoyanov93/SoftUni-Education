def user_check(force_dict: dict, user: str):
    for user_list in force_dict.values():
        if user in user_list:
            return True

    return False


my_dict = {}

command = input()
while command != "Lumpawaroo":
    if " | " in command:
        force_side, force_user = command.split(" | ")

        if force_side not in my_dict and not user_check(my_dict, force_user):
            my_dict[force_side] = []
            my_dict[force_side].append(force_user)
        elif not user_check(my_dict, force_user):
            my_dict[force_side].append(force_user)
        elif user_check(my_dict, force_user):
            pass

    elif " -> " in command:
        force_user, force_side = command.split(" -> ")

        if force_side not in my_dict and not user_check(my_dict, force_user):
            my_dict[force_side] = []
            my_dict[force_side].append(force_user)
            print(f"{force_user} joins the {force_side} side!")
        elif not user_check(my_dict, force_user):
            my_dict[force_side].append(force_user)
            print(f"{force_user} joins the {force_side} side!")
        elif user_check(my_dict, force_user):
            for side, user in my_dict.items():
                if force_user in user:
                    my_dict[side].remove(force_user)
            my_dict[force_side].append(force_user)
            print(f"{force_user} joins the {force_side} side!")

    command = input()

for (side, users) in sorted(my_dict.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])):
    if len(my_dict[side]) > 0:
        print(f"Side: {side}, Members: {len(my_dict[side])}")
        for user1 in sorted(users):
            print(f"! {user1}")
