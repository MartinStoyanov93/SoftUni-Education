record = float(input())
distance = float(input())
time_per_meter = float(input())


time_to_finish = distance * time_per_meter
delay = (distance // 15) * 12.5
total_time = time_to_finish + delay

if total_time >= record:
    exact_time = total_time - record
    print(f"No, he failed! He was {exact_time:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")