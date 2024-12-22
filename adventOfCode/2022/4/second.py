
inputText = []
while True:
    try:
        line = input()
    except:
        break
    inputText.append(line)

total = 0
for line in inputText:
    range_sections = line.split(",")
    range1 = range_sections[0].split("-")
    range2 = range_sections[1].split("-")

    range1_start = int(range1[0])
    range1_end = int(range1[1])

    range2_start = int(range2[0])
    range2_end = int(range2[1])

    if (range1_start <= range2_start):
        if (range1_end >= range2_start):
            total += 1
    else:
        if (range2_end >= range1_start):
            total += 1

print(f"Total: {total}")
