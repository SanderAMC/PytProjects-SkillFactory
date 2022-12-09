game_field = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
weights = [4, 2, 4, 2, 6, 2, 4, 2, 4]
win_condition = False
comp_move, sap_move = False, False
comp_sign = ""

def draw_board():
    print("       1  2  3\n")
    for i in range(3):
        line = "   " + str(i+1) + "  "
        for j in range(3):
            line += " " + game_field[3 * i + j] + " "

        for j in range(3):
            line += "  " + str(weights[3 * i + j])
        print(line)
    print("\n")
    return

def sap_get_move():
    while True:
        s = input("Введите строку и столбец 1 .. 3, куда пойдете (через пробел). Ввод 0 означает выход из игры :")
        if s == "0":
            break

        if len(s) < 3 or not s[0].isdigit() or not s[2].isdigit() or int(s[0]) > 3 or int(s[2]) > 3:
            print("Не ошибайтесь при вводе.")
            continue

        if game_field[(int(list(s.split())[0])-1) * 3 + int(list(s.split())[1])-1] != "_":

            print("\nУже занято!")
            draw_board()
        else:
            break
    return s

def comp_get_move():
    max_index = weights.index(max(weights))
    max_weight = weights[max_index]
    print("Максимальный вес = ", max_weight)
    if max_weight != 0:
        game_field[max_index] = comp_sign
        weights[max_index] = 0
    else:
        print("Ошибка, что-то с индексами")

    return max_index

def recalc_weights(sign):
    for i in range(9):

        if i == 0 and game_field[i] == sign:
            if weights[2] != 0: weights[2] += 1
            if weights[6] != 0: weights[6] += 1
            if weights[8] != 0: weights[8] += 2
            print("Для 0 ячейки обработаны веса.")
        if i == 2 and game_field[i] == sign:
            if weights[0] != 0: weights[0] += 1
            if weights[6] != 0: weights[6] += 2
            if weights[8] != 0: weights[8] += 1
            print("Для 2 ячейки обработаны веса.")
        if i == 6 and game_field[i] == sign:
            if weights[2] != 0: weights[2] += 2
            if weights[0] != 0: weights[0] += 1
            if weights[8] != 0: weights[8] += 1
            print("Для 6 ячейки обработаны веса.")
        if i == 8 and game_field[i] == sign:
            if weights[2] != 0: weights[2] += 2
            if weights[0] != 0: weights[0] += 1
            if weights[6] != 0: weights[6] += 1
            print("Для 8 ячейки обработаны веса.")

        if weights[i] != 0:
            print((i, weights[i]))
            if i > 0 and i // 3 == (i-1) // 3 and game_field[i-1] == sign:
                print("слева + 1")
                weights[i] +=1
            if i < 8 and i // 3 == (i+1) // 3 and game_field[i+1] == sign:
                print("справа + 1")
                weights[i] +=1
            if i > 2 and game_field[i-3] == sign:
                print("сверху + 1")
                weights[i] += 1
            if i < 6 and game_field[i+3] == sign:
                print("снизу + 1")
                weights[i] += 1



def check_win(board):
    X_ = "X" * 3
    O_ = "O" * 3
    r = []

    r.append("".join(board[0:3]))
    r.append("".join(board[3:6]))
    r.append("".join(board[6:9]))
    r.append("".join(board[0:9:3]))
    r.append("".join(board[1:9:3]))
    r.append("".join(board[2:9:3]))
    r.append("".join(board[0:9:4]))
    r.append("".join(board[2:8:2]))

    if X_ in r:
        return "X"
    elif O_ in r:
        return "O"
    elif "_" not in game_field:
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
        sap_move, comp_move = True, False
        draw_board()
    else:
        print("Вы выбрали Нолик. Компьютер делает первый ход!")
        comp_sign, sap_sign = "X", "O"
        sap_move, comp_move = False, True

    while win_condition not in ["X", "O", "XO"]:

        if sap_move:
            move = sap_get_move()
            if move == "0":
                break
            ind_move = (int(list(move.split())[0]) - 1) * 3 + (int(list(move.split())[1]) - 1 )
            game_field[ind_move] = sap_sign
            weights[ind_move] = 0
            sap_move, comp_move = False, True
            recalc_weights(sap_sign)
            print("Поле после вашего хода:")
            draw_board()

        else:
            ind_move = comp_get_move()
            sap_move, comp_move = True, False
            recalc_weights(comp_sign)
            print("Поле после хода компьютера:")
            draw_board()

        win_condition = check_win(game_field)

    if win_condition == comp_sign:
        print("Компьютер победил")
    elif win_condition == sap_sign:
        print("Вы победили. Компьютер позорно слил!")
    elif win_condition == "XO":
        print("Ничья, увы.")
    else:
        print("Вы выбрали прервать игру. Вы сдались, а компьютер молодец! До свиданья.")


