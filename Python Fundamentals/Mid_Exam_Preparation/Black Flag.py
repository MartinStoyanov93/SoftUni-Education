length_days = int(input())
plunder_per_day = int(input())
expected_plunder = float(input())

total_plunder = 0

for day in range(1, length_days + 1):

    if day % 3 == 0:
        total_plunder += plunder_per_day + (plunder_per_day * 0.5)
    elif day % 5 == 0:
        total_plunder += plunder_per_day
        total_plunder -= total_plunder * 0.3
    else:
        total_plunder += plunder_per_day

if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
elif total_plunder < expected_plunder:
    percentage = (total_plunder / expected_plunder) * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")
