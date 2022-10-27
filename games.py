from tabulate import tabulate
import emoji

def game_play(player_name, char, mat_game):
    print(f'Ход игрока {player_name}')
    headers_table = ['GAMETABLE']
    mui_player_one = (input('Ваш ход, введите цифру : '))
    for i in range(len(mat_game)):
        for j in range(len(mat_game)):
            if mui_player_one == mat_game[i][j] and mat_game[i][j] != emoji.emojize(':x:') and mat_game[i][
                j] != emoji.emojize(':o:'):
                mat_game[i][j] = char

    print(tabulate(mat_game, headers=headers_table, tablefmt='fancy_grid'))

    return mat_game