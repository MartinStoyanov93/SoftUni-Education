n = int(input())  #Период

treated_patients = 0
untreated_patients = 0
total_treated = 0
total_untreated = 0
doctors = 7

for i in range(1, n + 1):
    patients = int(input())
    if i % 3 == 0:
        if total_untreated > total_treated:
            doctors += 1
    if patients <= doctors:
        treated_patients += patients
        total_treated += patients
    else:
        treated_patients += doctors
        untreated_patients += patients - doctors
        total_untreated += patients - doctors

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")