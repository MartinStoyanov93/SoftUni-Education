wagons = int(input())

train = [0] * wagons

command = input()
while not command == "End":
    people = command.split()
    if people[0] == "add":
        train[-1] += int(people[1])
    elif people[0] == "insert":
        index = int(people[1])
        n_people = int(people[2])
        train[index] += int(n_people)
    elif people[0] == "leave":
        index = int(people[1])
        n_people = int(people[2])
        train[index] -= int(n_people)

    command = input()

print(train)

