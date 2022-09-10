n = int(input())
salary = int(input())

for i in range(n):
    tabs = input()
    if tabs == "Facebook":
        salary -= 150
    elif tabs == "Instagram":
        salary -= 100
    elif tabs == "Reddit":
        salary -= 50

    if salary <= 0:
        print("You have lost your salary.")
        break

if salary > 0:
    print(salary)







