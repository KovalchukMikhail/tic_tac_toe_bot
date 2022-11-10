from random import randint

win_game = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

def game_computer(current_position_player: list, current_position_computer: list, level: str):
    check_position_player = [0, 0, 0, 0, 0, 0, 0, 0]
    check_position_computer = [0, 0, 0, 0, 0, 0, 0, 0]
    count_player = 0
    count_computer = 0
    result: int
    for i in range(len(win_game)):
        for j in win_game[i]:
            if j in current_position_player:
                count_player += 1
            if j in current_position_computer:
                count_computer += 1
        check_position_player[i] = count_player
        check_position_computer[i] = count_computer
        count_player = 0
        count_computer = 0

    if level == 'easy':
        while True:
            result = randint(0, 8)
            if result not in current_position_player and result not in current_position_computer:
                return result

    if level == 'normal':
        while True:
            temp = randint(0, 1)
            if temp == 0:
                result = randint(0, 8)
                if result not in current_position_player and result not in current_position_computer:
                    return result
            else:
                break


    for i in range(len(check_position_computer)):
        if check_position_computer[i] == 2:
            for j in win_game[i]:
                if (j not in current_position_computer) and (j not in current_position_player):
                    result = j
                    return result

    for i in range(len(check_position_player)):
        if check_position_player[i] == 2:
            for j in win_game[i]:
                if (j not in current_position_computer) and (j not in current_position_player):
                    result = j
                    return result

    if 1 in check_position_computer:
        while True:
            current = randint(0, 7)
            if check_position_computer[current] == 1:
                for i in win_game[current]:
                    if (i not in current_position_computer) and (i not in current_position_player):
                        result = i
                        return result

    if 4 not in current_position_player:
        result = 4
        return result

    if 1 in check_position_player:
        while True:
            current = randint(0, 7)
            if check_position_player[current] == 1:
                for i in win_game[current]:
                    if (i not in current_position_computer) and (i not in current_position_player):
                        result = i
                        return result

def check_game(list_position):
    count = 0
    for i in range(len(win_game)):
        for j in win_game[i]:
            if j in list_position:
                count += 1
        if count == 3:
            return True
        count = 0
    return False







