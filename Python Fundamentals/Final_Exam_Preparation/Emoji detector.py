import re
text = input()

threshold = 1
thres_count = 0
my_emoji_dict = {}

pattern = r"(?P<emoji>\*{2}[A-Z]+[a-z]{2,}\*{2}|\:{2}[A-Z]+[a-z]{2,}\:{2})"
digit_pattern = r"(?P<digit>\d)"

digit_count = re.findall(digit_pattern, text)
for digit in digit_count:
    threshold *= int(digit)

matches_for_dict = re.finditer(pattern, text)
for match in matches_for_dict:
    emoji = match.group('emoji')
    my_emoji_dict[emoji] = 0

matches_for_count = re.findall(pattern, text)
for match in matches_for_count:
    for char in range(len(match)):
        if not match[char] == ":" and not match[char] == "*":
            current_value = ord(match[char])
            thres_count += current_value
    my_emoji_dict[match] = int(thres_count)
    thres_count = 0

print(f"Cool threshold: {threshold}")
print(f"{len(my_emoji_dict)} emojis found in the text. The cool ones are:")
for key, value in my_emoji_dict.items():
    if len(my_emoji_dict) > 0 and value > threshold:
        print(key)
