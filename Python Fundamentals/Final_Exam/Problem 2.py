import re
num_of_lines = int(input())
pattern = r"[A-Z]\$(?P<username>[A-Z]+[a-z]{2,})[A-Z]\$([A-Z]\@\$)(?P<password>[A-Za-z]{5,}[0-9]+)([A-Z]\@\$)"
count_matches = 0

data = input()
while num_of_lines > 0:
    num_of_lines -= 1

    if not re.fullmatch(pattern, data):
        print("Invalid username or password")
    else:
        matches = re.finditer(pattern, data)
        for match in matches:
            username = match.group("username")
            password = match.group("password")
            print("Registration was successful")
            print(f"Username: {username}, Password: {password}")
            count_matches += 1

    if num_of_lines == 0:
        print(f"Successful registrations: {count_matches}")
        break

    data = input()
