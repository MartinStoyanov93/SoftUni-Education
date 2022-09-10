import re

string = input()

pattern = r"\s(?P<email>(?P<user>[A-Za-z0-9]+[A-Za-z0-9\.\-\_]*)\@(?P<domain>[A-Za-z]+[A-Za-z\-]*(\.[A-Za-z\.]+)+))\b"

matches = re.finditer(pattern, string)

for match in matches:
    print(f"{match.group('email')}")

