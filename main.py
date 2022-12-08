game_field = [["O", "_", "_"], ["X", "X", "_"], ["_", "O", "_"]]
side = ""
win_condition = False
comp_move = ""

def draw_board():
    print("       1  2  3\n")
    for i in range(3):
        line = "   " + str(i+1) + "  "
        for j in range(3):
            line +=" " + game_field[i][j] + " "
        print(line)

    return

def get_move():
    return

def check_win():
    return ("o", True)


if __name__ == "__main__":

    print("Игра 'Крестики - нолики' на поле 3 х 3, с компьютером.")

    while side not in ["x", "o", "X", "O"]:
        side = input("Выберите, будете играть за 'Х' или за 'О' (x / o)? ")

    if side in ["X", "x"]:
        print("Вы выбрали игру за Крестики. Ваш ход первый.")
        comp_move = "o"
    else:
        print("Вы выбрали Нолик. Компьютер делает первый ход!")
        comp_move = "x"

    while not win_condition:
        draw_board()
        get_move()
        xo, win_condition = check_win()

    print("Компьютер победил") if xo == comp_move else print("Вы победили. Компьютер позорно слил!")

