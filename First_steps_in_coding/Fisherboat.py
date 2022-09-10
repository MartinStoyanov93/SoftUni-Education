mackerel = float(input())
caca = float(input())
palamud = float(input())
safrid = float(input())
seashells = int(input())

palamud_kg_price = mackerel + (mackerel * 0.60)
safrid_kg_price = caca + (caca * 0.80)

total_palamud = palamud_kg_price * palamud
total_safrid = safrid_kg_price * safrid
total_seashells = seashells * 7.50

total_price = total_palamud + total_safrid + total_seashells
print(f"{total_price:.2f}")