from tabulate import tabulate

def hi_one():
    print('🤑STARTGAME🤑')
    pl_one_name = input("Введите ваше имя : ")
    print(f'Привет , {pl_one_name}!')
    return pl_one_name
def hi_two():
    name_two_player = input("Введите имя второго игрока: ")
    print(f'Привет , {name_two_player}!')
    print()
    return name_two_player

def playing_table():
    matrix_game = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    headers_table = ['GAME ', 'for ', 'YOU ']
    print(tabulate(matrix_game, headers=headers_table, tablefmt='fancy_grid'))
    return matrix_game

def winner(count, random_move, pl_one_name, name_two_player):
    if count == True and random_move == 2:
        print(f' Победитель: {pl_one_name} ')
    elif count == True and random_move == 1:
        print(f' Победитель: {name_two_player} ')
    elif count == None:
        print('NO WINNER:')