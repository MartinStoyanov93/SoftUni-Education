course_dict = {}

data = input()
while not data == 'end':
    course_name, student_names = data.split(' : ')
    if course_name not in course_dict:
        course_dict[course_name] = []
    course_dict[course_name].append(student_names)

    data = input()

max_key = sorted(course_dict.items(), key=lambda x: (len(x[1])), reverse=True)
max_value = sorted(max_key, key=lambda x: (x[1]), reverse=False)
for course, student in max_key:
    print(f'{course}: {len(student)}')
    student = sorted(student, reverse=False)
    for el in student:
        print(f'-- {el}')