
inputText = []
while True:
    try:
        line = input()
    except EOFError:
        break
    inputText.append(line)

top_indexes = []
top_calories = []

top = 3

for _ in range(top):
    actual_elve = 0
    selected_elve = 0
    max_calories = 0
    total_calories = 0

    for line in inputText:
        try:
            total_calories += int(line)
        except ValueError:
            actual_elve += 1
            if not top_indexes.__contains__(actual_elve) and total_calories > max_calories:
                selected_elve = actual_elve
                max_calories = total_calories
            total_calories = 0
    top_calories.append(max_calories)
    top_indexes.append(selected_elve)

print(top_indexes)
print(top_calories)

print(f'sum top three calories: {sum(top_calories)}')
