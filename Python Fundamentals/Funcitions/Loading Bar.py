def loading_bar(percent):
    bar = []
    percent_count = 0
    bar_result = ""

    for i in range(0, 100, 10):
        if percent_count < percent:
            percent_count += 10
            bar.append("%")
        else:
            bar.append(".")

    for el in bar:
        bar_result += el

    if percent < 100:
        print(f"{percent}% [{bar_result}]")
        print("Still loading...")
    else:
        print(f"{percent}% Complete!")
        print(f"[{bar_result}]")


(loading_bar(int(input())))






