def factorial_division(num_1, num_2):
    num_counter_1 = 1
    num_counter_2 = 1
    for i in range(num_1, 0, -1,):
        num_counter_1 = num_counter_1 * i

    for j in range(num_2, 0, -1):
        num_counter_2 = num_counter_2 * j

    result = num_counter_1 / num_counter_2

    return f"{result:.2f}"


print(factorial_division(int(input()), int(input())))