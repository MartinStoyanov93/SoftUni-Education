days = int(input())
total_hours = int(input())
total_sum = 0

for day in range(1, days + 1):
    sum_per_day = 0
    for h in range(1, total_hours + 1):
        if day % 2 == 0 and h % 2 == 1:
            sum_per_day += 2.50
        elif day % 2 == 1 and h % 2 == 0:
            sum_per_day += 1.25
        else:
            sum_per_day += 1

    print(f"Day: {day} - {sum_per_day:.2f}")
    total_sum += sum_per_day

print(f"Total: {total_sum:.2f} leva")




