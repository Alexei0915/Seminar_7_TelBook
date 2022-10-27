import random
import games as gp
import emoji


def game_start(pl_one_name, name_two_player, matrix_game):
    random_move = random.randint(1, 2)
    count = False
    count_len = 9
    while count == False:
        if random_move == 1:
            gp.game_play(pl_one_name, emoji.emojize('🧿'), matrix_game)
            count = count_games(matrix_game)
            random_move = 2
            count_len -= 1
        elif random_move == 2:
            gp.game_play(name_two_player, emoji.emojize('❌'), matrix_game)
            count = count_games(matrix_game)
            random_move = 1
            count_len -= 1
        if count_len == 0:
            count = None

    return count, random_move


def count_games(mat_game):
    if mat_game[0][0] == mat_game[0][1] == mat_game[0][2]:
        return True
    elif mat_game[1][0] == mat_game[1][1] == mat_game[1][2]:
        return True
    elif mat_game[2][0] == mat_game[2][1] == mat_game[2][2]:
        return True
    elif mat_game[0][0] == mat_game[1][0] == mat_game[2][0]:
        return True
    elif mat_game[0][1] == mat_game[1][1] == mat_game[2][1]:
        return True
    elif mat_game[0][2] == mat_game[1][2] == mat_game[2][2]:
        return True
    elif mat_game[0][0] == mat_game[1][1] == mat_game[2][2]:
        return True
    elif mat_game[2][0] == mat_game[1][1] == mat_game[0][2]:
        return True
    else:
        return False