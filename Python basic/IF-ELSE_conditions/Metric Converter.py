number = float(input())
entrace_unit = str(input())
exit_unit = str(input())

if entrace_unit == "mm" and exit_unit == "m":
    number = number / 1000
    print(f"{number:.3f}")
elif entrace_unit == "mm" and exit_unit == "cm":
    number = number / 10
    print(f"{number:.3f}")
elif entrace_unit == "cm" and exit_unit == "m":
    number = number / 100
    print(f"{number:.3f}")
elif entrace_unit == "cm" and exit_unit == "mm":
    number = number * 10
    print(f"{number:.3f}")
elif entrace_unit == "m" and exit_unit == "mm":
    number = number * 1000
    print(f"{number:.3f}")
elif entrace_unit == "m" and exit_unit == "cm":
    number = number * 100
    print(f"{number:.3f}")

