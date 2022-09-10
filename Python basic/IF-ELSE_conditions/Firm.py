import math


project_time = int(input())
time_given = int(input())
workers = int(input())

working_days = time_given - (time_given * 0.1)
work_hours = working_days * 8
extra_hours = (workers * 2) * time_given
total_work_hours = math.floor(work_hours + extra_hours)

if total_work_hours >= project_time:
    hours_left = total_work_hours - project_time
    print(f"Yes!{hours_left} hours left.")
else:
    hours_needed = project_time - total_work_hours
    print(f"Not enough time!{hours_needed} hours needed.")