students = int(input())
course_lectures = int(input())
additional_bonus = int(input())
students_attendance_list = []
max_bonus = 0
max_lectures = 0


while not students == 0:
    student_attend = int(input())
    students_attendance_list.append(student_attend)
    students -= 1


for el in students_attendance_list:
    total_bonus = (el / course_lectures) * (5 + additional_bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus

for i in students_attendance_list:
    if i > max_lectures:
        max_lectures = i

print(f"Max Bonus: {round(max_bonus)}.")
print(f"The student has attended {max_lectures} lectures.")
