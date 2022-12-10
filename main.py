import random

# Основное игровое поле
game_field = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]

win_condition = False
comp_move = None
comp_sign = ""

# Признак первого хода компа.
# В этом случае выбирается случайная ячейка из угловых и центральной,
# чтобы не тратить время минмакс на перебор пустого игрового поля
first_comp_move = True


def draw_board(board):
# Отрисовывает игровую доску 'board'

    print("       1  2  3\n")
    for i in range(3):
        line = "   " + str(i+1) + "  "
        for j in range(3):
            line += " " + board[3 * i + j] + " "

        print(line)
    print("\n")
    return


def get_possible_moves(board):
# Возвращает список доступных для хода ячеек на доске 'board'

    possiblemoves = []
    for i in range(3):
        for j in range(3):
            if board[3 * i + j] == "_":
                possiblemoves.append(3 * i + j)
    return possiblemoves


def sap_get_move():
# Принимает ввод пользователя для выбора хода. Возвращает номер строки и столбца через пробел.

    while True:
        s = input("Введите строку и столбец 1 .. 3, куда пойдете (через пробел). Ввод 0 означает выход из игры :")
        if s == "0":
            break

        if len(s) < 3 or not s[0].isdigit() or not s[2].isdigit() or int(s[0]) > 3 or int(s[2]) > 3:
            print("Не ошибайтесь при вводе.")
            continue

        if game_field[(int(list(s.split())[0])-1) * 3 + int(list(s.split())[1])-1] != "_":
            print("\nУже занято!")
            draw_board(game_field)
        else:
            break
    return s


def comp_get_move(first_move):
# Выбор хода компьютера. Используется алгоритм минмакс. На входе признак первого хода за компьютер.
# Выход - индекс ячейки с максимальным весом.

#    Общая логика алгоритма
#    1. копируем игровое поле
#    2. берем список доступных ячеек и идем по нему
#    3. делаем ход компа в копию игрового поля в очередную свободную ячейку и запускаем минмакс
#    4. в минмакс проверяем победу - если ход компа возвращаем +10; ничья - 0, ход игрока возвращаем -10
#    5. если нет победы - берем оставшиеся свободные ячейки и для них запускаем минмакс с ходом другого игрока
#    6. вернувшись из минмакс запоминаем очки для этой ячейки списка, отменяем ход, продолжаем п.3
#    7. если все свободные ячейки закончились - выбираем максимум очков и номер этой ячейки

    if first_move:
        while True:
            choice = random.choice(["0", "2", "4", "6", "8"])
            if game_field[int(choice)] == "_":
                return int(choice)

    scores = -10000000
    index = -1
    board_copy = game_field.copy()

    for i in get_possible_moves(board_copy):
        board_copy[i] = comp_sign
        cur_score = minmax(board_copy, False, sap_sign)
        if cur_score > scores:
            scores = cur_score
            index = i
        board_copy[i] = "_"

    return index


def minmax(board, ismax, sign):
# Итерационная функция поиска весов.
# Возвращает +10 для победы ходом компа, -10 для победы ходом человека и 0 в случае ничьей.

# Основное условия выхода рекурсии, при оценке победы любой из сторон или ничьей
    res = check_win(board)
    if res in ["X", "O"] and not ismax:
        return 10
    elif res in ["X", "O"] and ismax:
        return -10
    elif res == "XO":
        return 0

# Если победы еще нет, рекурсивно оцениваем веса оставшихся возможных ходов
    minmax_score = []
    for k in get_possible_moves(board):
        board[k] = sign
        if sign == sap_sign:
            minmax_score.append(minmax(board, not ismax, comp_sign))
        else:
            minmax_score.append(minmax(board, not ismax, sap_sign))
        board[k] = "_"

    return max(minmax_score) if ismax else min(minmax_score)


def check_win(board):
# Проверяет условия победы за Х, О или ничьей на доске 'board'.
# Возвращает соответственно Х, О или ХО (ничья). Если нет победы или остаются ходы, то None

    x_ = "X" * 3
    o_ = "O" * 3
    r = []

    r.append("".join(board[0:3]))
    r.append("".join(board[3:6]))
    r.append("".join(board[6:9]))
    r.append("".join(board[0:9:3]))
    r.append("".join(board[1:9:3]))
    r.append("".join(board[2:9:3]))
    r.append("".join(board[0:9:4]))
    r.append("".join(board[2:8:2]))

    if x_ in r:
        return "X"
    elif o_ in r:
        return "O"
    elif "_" not in board:
        return "XO"

    return


if __name__ == "__main__":
    print("Игра 'Крестики - нолики' на поле 3 х 3, с компьютером. \n Ход начинают крестики.")

    side = ""
    while side not in ["x", "o", "X", "O"]:
        side = input("Выберите, будете играть за 'Х' или за 'О' (x / o)? ")

    if side in ["X", "x"]:
        print("Вы выбрали игру за Крестики. Ваш ход первый.")
        comp_sign, sap_sign = "O", "X"
        comp_move = False
        draw_board(game_field)
    else:
        print("Вы выбрали Нолик. Компьютер делает первый ход!")
        comp_sign, sap_sign = "X", "O"
        comp_move = True

# Основной игровой цикл
    while win_condition not in ["X", "O", "XO"]:

        if not comp_move:
            move = sap_get_move()
            if move == "0":
                break
            ind_move = (int(list(move.split())[0]) - 1) * 3 + (int(list(move.split())[1]) - 1)
            game_field[ind_move] = sap_sign
            comp_move = True

            print("Поле после вашего хода:")
            draw_board(game_field)

        else:
            ind_move = comp_get_move(first_comp_move)
            if first_comp_move:
                first_comp_move = False
            comp_move = False
            game_field[ind_move] = comp_sign
            print("Поле после хода компьютера:")
            draw_board(game_field)

        win_condition = check_win(game_field)

    if win_condition == comp_sign:
        print("Компьютер победил. Человеки совсем не умеют играть!")
    elif win_condition == sap_sign:
        print("Вы победили. Компьютер позорно слил! Но в следующий раз ...")
    elif win_condition == "XO":
        print("Ничья, увы. Как недостойно великого компьютера!")
    else:
        print("Вы выбрали прервать игру. Вы сдались, а компьютер молодец! До свиданья.")
