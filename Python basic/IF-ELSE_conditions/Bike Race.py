junior_cyclist = int(input())
senior_cyclist = int(input())
trace_type = input()

junior_sum = 0
senior_sum = 0
cyclist_count = junior_cyclist + senior_cyclist

if trace_type == "trail":
    junior_sum = junior_cyclist * 5.50
    senior_sum = senior_cyclist * 7
elif trace_type == "cross-country":
    if cyclist_count >= 50:
        junior_sum = (junior_cyclist * 8) - ((junior_cyclist * 8) * 0.25)
        senior_sum = (senior_cyclist * 9.50) - ((senior_cyclist * 9.50) * 0.25)
    else:
        junior_sum = junior_cyclist * 8
        senior_sum = senior_cyclist * 9.50
elif trace_type == "downhill":
    junior_sum = junior_cyclist * 12.25
    senior_sum = senior_cyclist * 13.75
elif trace_type == "road":
    junior_sum = junior_cyclist * 20
    senior_sum = senior_cyclist * 21.50

total_sum = junior_sum + senior_sum
expense = total_sum * 0.05
total_sum -= expense
print(f"{total_sum:.2f}")
