first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
total_people = int(input())

time = 0
total_answer_per_hour = first_employee + second_employee + third_employee


while True:
    if total_people > 0:
        time += 1
        total_people -= total_answer_per_hour
        if time % 4 == 0:
            time += 1
    else:
        break

print(f"Time needed: {time}h.")