count = 0
palindrome_list = []

words = input().split()
palindrome = input()

for el in words:
    if el == el[::-1]:
        palindrome_list.append(el)
    if el == palindrome:
        count += 1

print(palindrome_list)
print(f"Found palindrome {count} times")

