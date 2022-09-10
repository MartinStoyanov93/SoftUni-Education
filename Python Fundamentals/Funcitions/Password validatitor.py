
def password_validator(password):
    is_valid = True
    digit_counter = 0

    if 6 > len(password) <= 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False

    if not password.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False

    for char in password:
        if char.isdigit():
            digit_counter += 1

    if digit_counter < 2:
        is_valid = False
        print("Password must have at least 2 digits")

    return is_valid


input_password = input()
output = password_validator(input_password)

if output:
    print("Password is valid")

