# You will receive a single number n. On the next n lines you will receive names of courses.
# You should create a list of courses and print it.

number = int(input())
list = []

for name in range(number):
    course = input()
    list.append(course)

print(list)