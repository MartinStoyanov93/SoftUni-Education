pool_volume = int(input())
pipe1 = int(input())
pipe2 = int(input())
hours = float(input())

p1 = pipe1 * hours
p2 = pipe2 * hours

total_water = p1 + p2

if total_water < pool_volume:
    total_water_percent = total_water / pool_volume * 100
    p1_percent = p1 / total_water * 100
    p2_percent = p2 / total_water * 100
    print(f"The pool is {total_water_percent:.2f}% full.")
    print(f"Pipe 1: {p1_percent:.2f}%.")
    print(f"Pipe 2: {p2_percent:.2f}%.")
else:
    overflow = total_water - pool_volume
    print(f"For {hours:.2f} the pool overflows with {overflow:.2f} liters.")