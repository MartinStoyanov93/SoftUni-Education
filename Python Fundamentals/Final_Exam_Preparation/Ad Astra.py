string = list(input())
result = []

while len(string) > 0:
    result.append(string.pop())

print(f"{''.join(result)}")
