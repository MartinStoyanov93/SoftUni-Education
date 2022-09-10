elements = input().split()
my_dict = {}

for word in elements:
    lower_case_word = word.lower()
    if lower_case_word not in my_dict:
        my_dict[lower_case_word] = 1
    else:
        my_dict[lower_case_word] += 1

for key, value in my_dict.items():
    if not value % 2 == 0:
        print(key, end=" ")



