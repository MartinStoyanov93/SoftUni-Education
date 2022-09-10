import re

text = input()


pattern = r'\b\_(?P<variable_name>[A-Za-z0-9]+)\b'
valid_variable = []

matches = re.finditer(pattern, text)
matches = [valid_variable.append(match.group('variable_name')) for match in matches]
print(','.join(valid_variable))
