employees_happiness = input().split(" ")
happiness_multiplier = int(input())

total_happiness = ([int(i) * happiness_multiplier for i in employees_happiness])

average_happiness = (sum(total_happiness) / len(total_happiness))

counter = len([employee for employee in total_happiness if employee > average_happiness])

if counter >= len(employees_happiness) / 2:
    print(f"Score: {counter}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {counter}/{len(employees_happiness)}. Employees are not happy!")

