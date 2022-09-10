years = float(input())
gender = str(input())

if gender == "m":
    if years < 16:
        print("Master")
    else:
        print("Mr.")

if gender == "f":
    if years < 16:
        print("Miss")
    else:
        print("Ms.")