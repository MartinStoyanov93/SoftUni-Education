total_sheets = int(input())
sheets_per_hour = int(input())
days = int(input())

total_read_time = total_sheets / sheets_per_hour
hours_per_day = total_read_time / days
print(hours_per_day)