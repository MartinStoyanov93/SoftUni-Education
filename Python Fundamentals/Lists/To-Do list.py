temporary_list = [0] * 10

command = input()
while not command == "End":
    priority, note = command.split("-")
    priority_index = int(priority) - 1
    temporary_list[priority_index] = note

    command = input()

result = [index for index in temporary_list if index != 0]
print(result)
