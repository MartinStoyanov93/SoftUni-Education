n1 = int(input()) #капацитет на стадион
n2 = int(input()) #брой фенове

sector_A = 0
sector_B = 0
sector_V = 0
sector_G = 0

for i in range(n2):
    sector = input()
    if sector == "A":
        sector_A += 1
    elif sector == "B":
        sector_B += 1
    elif sector == "V":
        sector_V += 1
    elif sector == "G":
        sector_G += 1

percentA = (sector_A / n2) * 100
print(f"{percentA:.2f}%")
percentB = (sector_B / n2) * 100
print(f"{percentB:.2f}%")
percentV = (sector_V / n2) * 100
print(f"{percentV:.2f}%")
percentG = (sector_G / n2) * 100
print(f"{percentG:.2f}%")
TotalPercent = (n2 / n1) * 100
print(f"{TotalPercent:.2f}%")
