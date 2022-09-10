#	Торта  – цената ѝ е 20% от наема на залата
#Напитки – цената им е 45% по-малко от тази на тортата
#	Аниматор – цената му е 1/3 от цената за наема на залата

rent = int(input())

cake = rent * 0.20
drinks = cake - cake * 0.45
animator = rent * 1/3
total_price = cake + drinks + animator + rent
print(total_price)