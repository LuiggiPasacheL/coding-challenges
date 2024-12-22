
inputText = []
while True:
    try:
        line = input()
    except EOFError:
        break
    inputText.append(line)

total_calories = 0
actual_elve = 0
maxInt = 0
for line in inputText:
    try:
        calorie = int(line) 
        total_calories += calorie
    except ValueError:
        actual_elve += 1
        if total_calories > maxInt:
            maxInt = total_calories
        total_calories = 0

print(f'Maximun value: {maxInt}')
print(f'Elve with maximun value: {actual_elve}')
