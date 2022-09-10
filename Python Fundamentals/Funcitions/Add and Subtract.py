def add_and_subtract(num1, num2, num3):

    def sum_numbers():
        sum_of_elements = num1 + num2

        return sum_of_elements

    def subtract():
        diff = sum_numbers() - num3

        return diff

    return subtract()


print(add_and_subtract(num1=int(input()), num2=int(input()), num3=int(input())))



