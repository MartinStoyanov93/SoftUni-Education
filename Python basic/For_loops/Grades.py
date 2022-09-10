n = int(input())

total_grade = 0
failed = 0
average = 0
good = 0
top = 0

for i in range(n):
    grade = float(input())
    if 2 <= grade <= 2.99:
        failed += 1
        total_grade += grade
    elif 3 <= grade <= 3.99:
        average += 1
        total_grade += grade
    elif 4 <= grade <= 4.99:
        good += 1
        total_grade += grade
    else:
        top += 1
        total_grade += grade

Average_grade = total_grade / n
failed_percent = (failed / n) * 100
average_percent = (average / n) * 100
good_percent = (good / n) * 100
top_percent = (top / n) * 100

print(f"Top students: {top_percent:.2f}%")
print(f"Between 4.00 and 4.99: {good_percent:.2f}%")
print(f"Between 3.00 and 3.99: {average_percent:.2f}%")
print(f"Fail: {failed_percent:.2f}%")
print(f"Average: {Average_grade:.2f}")
