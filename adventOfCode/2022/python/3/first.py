
inputText = []
while True:
    try:
        line = input()
    except:
        break
    inputText.append(line)


def get_item_in_both_compartments(rucksack):
    elements = {}
    compartment_lenght = len(rucksack) / 2
    for index, item in enumerate(rucksack):
        if item not in elements and index < compartment_lenght:
            elements[item] = 1
        else:
            if item in elements and index >= compartment_lenght:
                elements[item] += 1
                return item

def get_value_for_item(item):
    item_ascii_value = ord(item)
    if item_ascii_value > 96: # if it is a letter in lowercase
        displace = 96
    else:
        displace = 38
    return item_ascii_value - displace

sum = 0
for line in inputText:
    rucksack = line.strip()
    item_in_both_compartments = get_item_in_both_compartments(rucksack)
    if item_in_both_compartments is not None:
        real_value_item = get_value_for_item(item_in_both_compartments)
        sum += real_value_item

print(sum)
