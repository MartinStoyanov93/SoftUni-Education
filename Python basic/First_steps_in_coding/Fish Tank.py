lenght_cm = int(input())
wide_cm = int(input())
height_cm = int(input())
volume_percent = int(input())

total_volume = lenght_cm * wide_cm * height_cm
total_liters = total_volume * 0.001
percent = volume_percent * 0.01
liters_needed = total_liters * (1-percent)
print(liters_needed)