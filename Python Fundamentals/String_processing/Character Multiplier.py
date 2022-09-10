string = input().split()
word_one = string[0]
word_two = string[1]
min_len_word = min(len(word_one), len(word_two))
max_len_word = max(len(word_one), len(word_two))

result = 0

for i in range(min_len_word):
    first_one_ch = word_one[i]
    first_two_ch = word_two[i]

    current_score = ord(first_one_ch) * ord(first_two_ch)
    result += current_score

for el in range(min_len_word, max_len_word):
    if len(word_one) > len(word_two):
        first_one_ch = word_one[el]
        result += ord(first_one_ch)
    else:
        first_two_ch = word_two[el]
        result += ord(first_two_ch)

print(result)