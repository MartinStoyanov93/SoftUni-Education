campaign_days = int(input())
total_bakers = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())

sum_cakes = cakes * 45
sum_waffles = waffles * 5.80
sum_pancakes = pancakes * 3.20

sum_per_day = (sum_cakes + sum_waffles + sum_pancakes) * total_bakers
total_sum = sum_per_day * 23
total_sum -= total_sum * 1/8
print(total_sum)
