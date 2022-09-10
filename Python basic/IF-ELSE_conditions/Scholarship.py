# Учениците могат да кандидатстват за социална стипендия или за стипендия за отличен успех. Изискване за
# социална стипендия - доход на член от семейството по-малък от минималната работна заплата и успех над
# 4.5. Размер на социалната стипендия - 35% от минималната работна заплата. Изискване за стипендия за
# отличен успех - успех над 5.5, включително. Размер на стипендията за отличен успех - успехът на ученика,
# умножен по коефициент 25.
# Напишете програма, която при въведени доход, успех и минимална работна заплата, дава информация дали
# ученик има право да получава стипендия, и стойността на стипендията, която е по-висока за него.
import math


salary = float(input())
grade = float(input())
minimum_wage = float(input())

scholarship_one = grade * 25
scholarship_two = salary * 0.35

if salary < minimum_wage and grade >= 4.50:
    if grade >= 5.50 and scholarship_two >= scholarship_one:
        print(f"You get a scholarship for excellent results {math.floor(scholarship)} BGN")
    else:
        print(f"You get a Social scholarship {math.floor(scholarship)} BGN")
elif grade >= 5.50:
    print(f"You get a scholarship for excellent results {math.floor(scholarship)} BGN")
else:
    print("You cannot get a scholarship!")