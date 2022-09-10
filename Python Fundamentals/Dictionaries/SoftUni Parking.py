number = int(input())
register_sheet = {}

data = input()
while not number == 0:
    command = data.split()

    if command[0] == "register":
        if command[1] not in register_sheet:
            register_sheet[command[1]] = command[2]
            print(f"{command[1]} registered {command[2]} successfully")
        else:
            print(f"ERROR: already registered with plate number {command[2]}")

    elif command[0] == "unregister":
        if command[1] not in register_sheet:
            print(f"ERROR: user {command[1]} not found")
        else:
            register_sheet.pop(command[1])
            print(f"{command[1]} unregistered successfully")

    number -= 1
    if number == 0:
        for key, value in register_sheet.items():
            print(f"{key} => {value}")
        break

    data = input()
