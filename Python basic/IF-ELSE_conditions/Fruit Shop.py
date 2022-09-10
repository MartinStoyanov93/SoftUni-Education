fruit = input()
day = input()
quantity = float(input())

if fruit == "banana":
    if day == "Saturday" or day == "Sunday":
        price = 2.70 * quantity
        print(f"{price:.2f}")
    elif day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
        price = 2.50 * quantity
        print(f"{price:.2f}")
    else:
        print("error")
elif fruit == "apple":
    if day == "Saturday" or day == "Sunday":
        price = 1.25 * quantity
        print(f"{price:.2f}")
    elif day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
        price = 1.20 * quantity
        print(f"{price:.2f}")
    else:
        print("error")
elif fruit == "orange":
    if day == "Saturday" or day == "Sunday":
        price = 0.90 * quantity
        print(f"{price:.2f}")
    elif day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
        price = 0.85 * quantity
        print(f"{price:.2f}")
    else:
        print("error")
elif fruit == "grapefruit":
    if day == "Saturday" or day == "Sunday":
        price = 1.60 * quantity
        print(f"{price:.2f}")
    elif day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
        price = 1.45 * quantity
        print(f"{price:.2f}")
    else:
        print("error")
elif fruit == "kiwi":
    if day == "Saturday" or day == "Sunday":
        price = 3.00 * quantity
        print(f"{price:.2f}")
    elif day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
        price = 2.70 * quantity
        print(f"{price:.2f}")
    else:
        print("error")
elif fruit == "pineapple":
    if day == "Saturday" or day == "Sunday":
        price = 5.60 * quantity
        print(f"{price:.2f}")
    elif day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
        price = 5.50 * quantity
        print(f"{price:.2f}")
    else:
        print("error")
elif fruit == "grapes":
    if day == "Saturday" or day == "Sunday":
        price = 4.20 * quantity
        print(f"{price:.2f}")
    elif day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
        price = 3.85 * quantity
        print(f"{price:.2f}")
    else:
        print("error")
else:
    print("error")