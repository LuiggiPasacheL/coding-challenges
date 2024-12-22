
inputText = []
while True:
    try:
        line = input()
    except:
        break
    inputText.append(line)

def get_badge(three_lines):
    elements = {}
    for line in three_lines:
        line_elements = dict.fromkeys(line, 1)
        for key in line_elements:
            if key not in elements:
                elements[key] = 1
            else:
                elements[key] += 1
                if elements[key] == 3:
                    return key
    return None

def get_value_for_item(item):
    item_ascii_value = ord(item)
    if item_ascii_value > 96: # if it is a letter in lowercase
        displace = 96
    else:
        displace = 38
    return item_ascii_value - displace

sum = 0
for index, line in enumerate(inputText):
    if index % 3 == 0:
        three_lines = inputText[index:index+3]
        badge = get_badge(three_lines)
        if badge is not None:
            sum += get_value_for_item(badge)

print(sum)
