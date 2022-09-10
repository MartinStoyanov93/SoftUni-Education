budget = float(input())
category = input()  # VIP or Normal
number_of_people = int(input())

transport = 0
tickets = 0

if category == "VIP":
    tickets = 499.99 * number_of_people
elif category == "Normal":
    tickets = 249.99 * number_of_people

if 1 <= number_of_people <= 4:
    transport = budget * 0.25
elif 5 <= number_of_people <= 9:
    transport = budget * 0.40
elif 10 <= number_of_people <= 24:
    transport = budget * 0.50
elif 25 <= number_of_people <= 49:
    transport = budget * 0.60
else:
    transport = budget * 0.75

if tickets < transport:
    total_sum = transport - tickets
    print(f"Yes! You have {total_sum:.2f} leva left.")
else:
    total_sum = tickets - transport
    print(f"Not enough money! You need {total_sum:.2f} leva.")