season = input()
group_type = input()
students_number = int(input())
total_days = int(input())

price = 0
sport = ""

if season == "Winter":
    if group_type == "boys":
        price = (total_days * 9.60) * students_number
        sport = "Judo"
    elif group_type == "girls":
        price = (total_days * 9.60) * students_number
        sport = "Gymnastic"
    elif group_type == "mixed":
        price = (total_days * 10) * students_number
        sport = "Ski"
elif season == "Spring":
    if group_type == "boys":
        price = (total_days * 7.20) * students_number
        sport = "Tennis"
    elif group_type == "girls":
        price = (total_days * 7.20) * students_number
        sport = "Athletics"
    elif group_type == "mixed":
        price = (total_days * 9.50) * students_number
        sport = "Cycling"
elif season == "Summer":
    if group_type == "boys":
        price = (total_days * 15) * students_number
        sport = "Football"
    elif group_type == "girls":
        price = (total_days * 15) * students_number
        sport = "Volleyball"
    elif group_type == "mixed":
        price = (total_days * 20) * students_number
        sport = "Swimming"

if students_number >= 50:
    price = price - (price * 0.5)
elif 20 <= students_number < 50:
    price = price - (price * 0.15)
elif 10 <= students_number < 20:
    price = price - (price * 0.05)

print(f"{sport} {price:.2f} lv.")



