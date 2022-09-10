# You will be given a number n. On the next n lines you will receive integers. You should create and print two lists
# ⦁	One with all the positives (including 0) numbers
# ⦁	One with all the negatives numbers

number = int(input())
positive_list = []
negative_list = []

for n in range(number):
    nums = int(input())
    if nums <= 0:
        negative_list.append(nums)
    else:
        positive_list.append(nums)

print(positive_list)
print(negative_list)
print(f"Count of positives: {len(positive_list)}. Sum of negatives: {sum(negative_list)}")