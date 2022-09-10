import re

text = input().lower()
word = input().lower()

pattern = rf"\b{word}\b"

result = len(re.findall(pattern, text))
print(result)