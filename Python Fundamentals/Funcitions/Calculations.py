input_operator = str(input())
first_num = int(input())
second_num = int(input())


def calculator(num1, num2, operator):
    result = None
    if operator == "multiply":
        result = num1 * num2
    elif operator == "divide":
        result = int(num1 / num2)
    elif operator == "add":
        result = num1 + num2
    elif operator == "subtract":
        result = num1 - num2

    return result


print(calculator(first_num, second_num, input_operator))


