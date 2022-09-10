def perfect_number():
    number = int(input())
    count = 0

    for el in range(1, number + 1):
        if number % el == 0:
            count += el

    if count / number == 2:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


perfect_number()