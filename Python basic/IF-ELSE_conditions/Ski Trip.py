days_spent = int(input())
room = input()
feedback = input()

nights = days_spent - 1
total_price = 0

if room == "apartment":
    if days_spent < 10:
        price = nights * 25.00
        discount = price * 0.3
        total_price = price - discount
    elif 10 <= days_spent <= 15:
        price = nights * 25.00
        discount = price * 0.35
        total_price = price - discount
    elif days_spent > 15:
        price = nights * 25.00
        discount = 25.00 * 0.5
        total_price = price - discount
elif room == "president apartment":
    if days_spent < 10:
        price = nights * 35.00
        discount = price * 0.1
        total_price = price - discount
    elif 10 <= days_spent <= 15:
        price = nights * 35.00
        discount = price * 0.15
        total_price = price - discount
    elif days_spent > 15:
        price = nights * 35.00
        discount = price * 0.2
        total_price = price - discount
elif room == "room for one person":
    total_price = 18.00 * nights

if feedback == "positive":
    positive_discount =  total_price * 0.25
    final_price = total_price + positive_discount
    print(f"{final_price:.2f}")
elif feedback == "negative":
    negative_feedback = total_price * 0.1
    final_price = total_price - negative_feedback
    print(f"{final_price:.2f}")