
def small_number():
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    if num1 < num2:
        output = num1
    elif num2 < num3:
        output = num2
    else:
        output = num3

    return output


print(small_number())

