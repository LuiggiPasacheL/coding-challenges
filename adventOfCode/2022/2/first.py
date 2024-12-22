
inputText = []
while True:
    try:
        line = input()
    except:
        break
    inputText.append(line)

oponent_rock = 'A'
oponent_paper = 'B'
oponent_scissors = 'C'

translate_movement = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

score_for_movement = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

score_for_result = {
    'W': 6,
    'D': 3,
    'L': 0
}

def get_score_for_movement(opponent_movement, my_movement):
    score = 0
    result = ''
    if translate_movement[opponent_movement] == my_movement:
        result = 'D'
    else:
        if opponent_movement == oponent_rock:
            if my_movement == 'Y':
                result = 'W'
            else:
                result = 'L'
        elif opponent_movement == oponent_paper:
            if my_movement == 'Z':
                result = 'W'
            else:
                result = 'L'
        elif opponent_movement == oponent_scissors:
            if my_movement == 'X':
                result = 'W'
            else:
                result = 'L'
    score += score_for_movement[my_movement] + score_for_result[result]
    return score


total_score = 0
for line in inputText:

    opponent_movement = line[0]
    my_movement = line[2]

    my_score = get_score_for_movement(opponent_movement, my_movement)
    print(my_score)
    total_score += my_score

print(total_score)
