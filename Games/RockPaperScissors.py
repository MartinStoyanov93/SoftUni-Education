import random


def play():
    print("Please choose:")
    user = input("'R' for rock,'P' for paper and 'C' for scissors: \n".lower())
    computer = random.choice(['r','p','s'])

    if user == computer:
        return "It's a Tie!"

    if is_win(user, computer):
        return "You won!"

    return "Loser!"


def is_win(player, opponent):

    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True

print(play())

