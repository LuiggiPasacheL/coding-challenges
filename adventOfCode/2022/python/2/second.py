
inputText = []
while True:
    try:
        line = input()
    except:
        break
    inputText.append(line)

need_win = 'Z'
need_draw = 'Y'
need_lose = 'X'

opponent_rock = 'A'
opponent_paper = 'B'
opponent_scissors = 'C'

my_rock = 'R'
my_paper = 'P'
my_scissors = 'S'

translate_movement = {
    'A': 'R',
    'B': 'P',
    'C': 'S'
}

score_for_movement = {
    'R': 1,
    'P': 2,
    'S': 3
}

score_for_result = {
    'W': 6,
    'D': 3,
    'L': 0
}

def get_movement(need, opponent_move):
    if opponent_move == opponent_rock:
        if need == need_win:
            return my_paper
        elif need == need_draw:
            return my_rock
        elif need == need_lose:
            return my_scissors
    elif opponent_move == opponent_paper:
        if need == need_win:
            return my_scissors
        elif need == need_draw:
            return my_paper
        elif need == need_lose:
            return my_rock
    elif opponent_move == opponent_scissors:
        if need == need_win:
            return my_rock
        elif need == need_draw:
            return my_scissors
        elif need == need_lose:
            return my_paper

def get_score_for_movement(opponent_movement, my_movement):
    score = 0
    result = ''
    if translate_movement[opponent_movement] == my_movement:
        result = 'D'
    else:
        if opponent_movement == opponent_rock:
            if my_movement == 'P':
                result = 'W'
            else:
                result = 'L'
        elif opponent_movement == opponent_paper:
            if my_movement == 'S':
                result = 'W'
            else:
                result = 'L'
        elif opponent_movement == opponent_scissors:
            if my_movement == 'R':
                result = 'W'
            else:
                result = 'L'
    score += score_for_movement[my_movement] + score_for_result[result]
    return score

total_score = 0
for line in inputText:
    opponent_movement = line[0]
    need = line[2]

    my_movement = get_movement(need, opponent_movement)

    score = get_score_for_movement(opponent_movement, my_movement)

    total_score += score

print(total_score)
