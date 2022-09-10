days_off = int(input())

norm = 30000

working_days = 365 - days_off
total_time_play = (working_days * 63) + (days_off * 127)

if total_time_play > norm:
    diff = total_time_play - norm
    H = diff // 60
    M = diff % 60
    print("Tom will run away")
    print(f"{H} hours and {M} minutes more for play")
else:
    diff = norm - total_time_play
    H = diff // 60
    M = diff % 60
    print("Tom sleeps well")
    print(f"{H} hours and {M} minutes less for play")