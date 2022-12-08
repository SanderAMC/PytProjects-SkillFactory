game_field = [["O", "_", "_"], ["X", "X", "_"], ["_", "O", "_"]]
side = ""
win_condition = False
comp_move, sap_move = False, False
comp_sign = ""

def draw_board():
    print("       1  2  3\n")
    for i in range(3):
        line = "   " + str(i+1) + "  "
        for j in range(3):
            line += " " + game_field[i][j] + " "
        print(line)
    print("\n")
    return

def sap_get_move():
    while True:
        s = input("Введите строку и столбец, куда пойдете (через пробел)?")
        if game_field[int(list(s.split())[0])-1][int(list(s.split())[1])-1] != "_":
            print("\nУже занято!")
            draw_board()
        else:
            break
    return s

def comp_get_move():
    return

def check_win():

    return ("o", True)


if __name__ == "__main__":

    print("Игра 'Крестики - нолики' на поле 3 х 3, с компьютером.")

    while side not in ["x", "o", "X", "O"]:
        side = input("Выберите, будете играть за 'Х' или за 'О' (x / o)? ")

    if side in ["X", "x"]:
        print("Вы выбрали игру за Крестики. Ваш ход первый.")
        comp_sign, sap_sign = "O", "X"
        sap_move, comp_move = True, False
    else:
        print("Вы выбрали Нолик. Компьютер делает первый ход!")
        comp_sign, sap_sign = "X", "O"
        sap_move, comp_move = False, True

    draw_board()
    while not win_condition:

        if sap_move:
            move = sap_get_move()
            game_field[int(list(move.split())[0]) - 1][int(list(move.split())[1]) - 1] = sap_sign
            sap_move, comp_move = False, True

        else:
            comp_get_move()
            sap_move, comp_move = True, False

        draw_board()
        #xo, win_condition = check_win()

    print("Компьютер победил") if xo == comp_move else print("Вы победили. Компьютер позорно слил!")

