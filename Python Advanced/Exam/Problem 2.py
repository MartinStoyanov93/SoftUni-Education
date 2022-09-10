def is_in_range(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


size = 6
matrix = []
for _ in range(size):
    elements = input().split()
    matrix.append(elements)


directions = {
    "up": (-1, 0),
    "down": (1, 0),
}

score = 0
throw_count = 0
hit_bucket = []
bucket_row, bucket_col = 0, 0
while True:
    if throw_count == 3:
        break
    coordinates = eval(input())
    bucket_row = coordinates[0]
    bucket_col = coordinates[1]
    throw_count += 1

    if not is_in_range(bucket_row, bucket_col, size) or not matrix[bucket_row][bucket_col] == "B":
        continue

    if matrix[bucket_row][bucket_col] == "B":
        if (bucket_row, bucket_col) not in hit_bucket:
            next_row, next_col = 0, 0
            for direction in directions:
                bucket_row, bucket_col = coordinates[0], coordinates[1]
                next_row, next_col = bucket_row, bucket_col
                for row in range(size):
                    next_row = bucket_row + directions[direction][0]
                    next_col = bucket_col + directions[direction][1]
                    if is_in_range(next_row, next_col, size):
                        score += int(matrix[next_row][next_col])
                        bucket_row, bucket_col = next_row, next_col

            hit_bucket.append((coordinates[0], coordinates[1]))


prize = None
if 100 <= score <= 199:
    prize = "Football"
elif 200 <= score <= 299:
    prize = "Teddy Bear"
elif score >= 300:
    prize = "Lego Construction Set"

if prize:
    print(f"Good job! You scored {score} points, and you've won {prize}.")
else:
    diff = 100 - score
    print(f"Sorry! You need {diff} points more to win a prize.")
