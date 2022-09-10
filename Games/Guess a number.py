import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Cold! You are too low. Try again")
        elif guess > random_number:
            print("Cold! You are too high. Try again")

    print("Congrats, correct!")


guess(10)