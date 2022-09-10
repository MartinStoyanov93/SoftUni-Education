def isPalindrome():
    list_of_number = input()
    list = list_of_number.split(", ")

    for el in list:
        if el == el[::-1]:
            is_true = True
            print(is_true)
        else:
            is_true = False
            print(is_true)


isPalindrome()
