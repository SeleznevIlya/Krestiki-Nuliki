board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']


def print_board(board):
    '''
    Печатаем поле board
    '''
    for i in range(3):
        print(board[0+i*3], board[1+i*3], board[2+i*3])


def players_input(token):
    """функция хода игроков,

     player_move = ввод номера ячейки для выполнения хода
     строка 22 :проверка того что введенное значение не выходит за рамки длины списка с полем
     строка 23: если поле не занято крестиком или ноликом, то на эту позицию ставится соответствующий символ
     """
    game_condition = False
    while not game_condition:
        player_move = int(input(f'Твой ход. Ставь {token}'))
        if player_move >= 1 and player_move <= 9:
            if board[player_move-1] not in 'XO':
                board[player_move-1] = token
                game_condition = True
            else:
                print('Эта ячейка уже занята. Выберите другую')
        else:
            print('Ошибка ввода. Введите число от 1 до 9!')
            continue

def victory_condition(board):
    '''
    Функция проверки условия победы
    В кортеже с кортежами внесены все выигрышные комбинации
    цикл пробегается по каждому кортежу и сравнивает ячейки ,
    если все 3 ячейки с соответствующими индексами из кортежа равны(имеют Х или О),
    то возвращается элемент победителя, который эквивалентен True
    '''
    vin_condition = ((0, 1, 2), (3, 4, 5),
                     (6, 7, 8), (0, 3, 6),
                     (1, 4, 7), (2, 5, 8),
                     (0, 4, 8), (2, 4, 6))
    for one in vin_condition:
        if board[one[0]] == board[one[1]] == board[one[2]] == 'X' \
                or board[one[0]] == board[one[1]] == board[one[2]] == 'O':
            return board[one[0]]
    return False

def main(board):
    """
    Главная функция для обработки всей игры
    Count необходим для смены хода(четный - 1 игрок, нечетный - 2 игрок)

    """
    count = 0
    win_player = False
    while not win_player:
        print_board(board) #печатаем поле на каждом ходу
        if count % 2 == 0: #ход первого игрока
            players_input('X')
        else:               #ход второго игрока
            players_input('O')
        count += 1
        if count > 4: #проверка условия победы
            check = victory_condition(board)
            if check: #==True
                if count % 2 == 0:
                    print(f'Выйграл игрок O')
                    win_player = True
                elif count % 2 == 1:
                    print('Выйграл игрок X')
                    win_player = True
                elif count == 9:
                    print('Ничья')
                    win_player = True
    print_board(board)


if __name__ == '__main__':
    main(board)




