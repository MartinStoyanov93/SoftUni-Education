banned_words = input().split(", ")
text = input()

for word in banned_words:
    while word in text:
        replaced_word = len(word) * "*"
        text = text.replace(word, replaced_word)

print(text)