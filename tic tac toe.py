field = [[" ", "1", "2", "3"],
         ["1", "*", "*", "*"],
         ["2", "*", "*", "*"],
         ["3", "*", "*", "*"]]


def show():
    for i in range(len(field)):
        for j in range(len(field[i])):
            print(field[i][j], end=" ")
        print()
    print()


def greet():
    print("Игра крестики - нолики!")
    print("-----------------------")
    print("  Вводим номер строки,")
    print("  затем номер столбца")
    print("         УДАЧИ!")
    print("-----------------------")


def ask(step):
    print(f'Ходит: {step}')

    while True:

        x = input("Введите номер строки: ")
        y = input("Введите номер столбца: ")

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 1 > x or x > 3 or 1 > y or y > 3:
            print(" Координаты вне диапазона! ")
            continue

        if field[x][y] != "*":
            print(" Клетка занята! ")
            continue

        else:
            field[x][y] = step
            break

    for i in range(len(field)):
        for j in range(len(field[i])):
            print(field[i][j], end=" ")
        print()
    print()


def chek_winner(step):
    if any([field[1][1] == field[1][2] == field[1][3] == step,
            field[2][1] == field[2][2] == field[2][3] == step,
            field[3][1] == field[3][2] == field[3][3] == step,
            field[1][1] == field[2][1] == field[3][1] == step,
            field[1][2] == field[2][2] == field[3][2] == step,
            field[1][3] == field[2][3] == field[3][3] == step,
            field[1][1] == field[2][2] == field[3][3] == step,
            field[3][1] == field[2][2] == field[1][3] == step]):
        print(f" {step} победил!")
        return True
    if not any("*" in row for row in field):
        print("  Ничья!")
        return True


greet()

show()

while True:
    ask("X")
    if chek_winner("X"):
        break
    ask("0")
    if chek_winner("0"):
        break
