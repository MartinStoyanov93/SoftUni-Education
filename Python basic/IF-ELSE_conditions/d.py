salary = float(input())
grade = float(input())
minimum_wage = float(input())

if float(salary) > float(minimum_wage) and grade < 4.5:
    print("You cannot get a scholarship!")