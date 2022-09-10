first_string = input()
second_sting = input()

while first_string in second_sting:
    second_sting = second_sting.replace(first_string, "")

print(second_sting)
