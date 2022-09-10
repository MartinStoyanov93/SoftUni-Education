number = int(input())
my_dict = {}

while not number == 0:
    student_name = input()
    grade = float(input())

    if student_name not in my_dict:
        my_dict[student_name] = [grade]
    else:
        my_dict[student_name].append(grade)

    number -= 1

for student, grade in my_dict.items():
    average_grade = sum(grade) / len(grade)
    my_dict[student] = average_grade

my_dict_copy = my_dict.copy()

for el in my_dict_copy:
    if my_dict_copy[el] < 4.50:
        my_dict.pop(el)

for key, value in sorted(my_dict.items(), key=lambda x: -x[1]):
    print(f"{key} -> {value:.2f}")
