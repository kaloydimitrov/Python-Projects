table_list = ['-', '-', '-',
              '-', '-', '-',
              '-', '-', '-']


def table():
    print(table_list[0] + "|" + table_list[1] + "|" + table_list[2])
    print(table_list[3] + "|" + table_list[4] + "|" + table_list[5])
    print(table_list[6] + "|" + table_list[7] + "|" + table_list[8])


def check_if_win():
    if table_list[0] != '-' and table_list[4] != '-' and table_list[8] != '-' and table_list[0] == table_list[4] and \
            table_list[4] == table_list[8]:
        return True, table_list[0]
    elif table_list[6] != '-' and table_list[4] != '-' and table_list[2] != '-' and table_list[6] == table_list[4] and \
            table_list[4] == table_list[2]:
        return True, table_list[6]
    elif table_list[0] != '-' and table_list[3] != '-' and table_list[6] != '-' and table_list[0] == table_list[3] and \
            table_list[3] == table_list[4]:
        return True, table_list[0]
    elif table_list[1] != '-' and table_list[4] != '-' and table_list[7] != '-' and table_list[1] == table_list[4] and \
            table_list[4] == table_list[7]:
        return True, table_list[1]
    elif table_list[2] != '-' and table_list[5] != '-' and table_list[8] != '-' and table_list[2] == table_list[5] and \
            table_list[5] == table_list[8]:
        return True, table_list[2]
    elif table_list[0] != '-' and table_list[1] != '-' and table_list[2] != '-' and table_list[0] == table_list[1] and \
            table_list[1] == table_list[2]:
        return True, table_list[0]
    elif table_list[3] != '-' and table_list[4] != '-' and table_list[5] != '-' and table_list[3] == table_list[4] and \
            table_list[4] == table_list[5]:
        return True, table_list[3]
    elif table_list[6] != '-' and table_list[7] != '-' and table_list[8] != '-' and table_list[6] == table_list[7] and \
            table_list[7] == table_list[8]:
        return True, table_list[6]


def game_over():
    if check_if_win():
        if check_if_win()[1] == 'O':
            return True, "Player (O) wins the game!"
        elif check_if_win()[1] == 'X':
            return True, "Player (X) wins the game!"
    elif "-" not in table_list:
        return True, "Match Draw!"


one_to_nine = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def input_checker(turn, x_or_o):
    is_digit = turn.isnumeric()
    while not is_digit:
        print("Incorrect answer!")
        turn = input(f"Position 1-9 ({x_or_o}): ")
        is_digit = turn.isnumeric()
    turn = int(turn) - 1

    while turn + 1 not in one_to_nine:
        print("Incorrect answer!")
        turn = int(input(f"Position 1-9 ({x_or_o}): ")) - 1

    if table_list[turn] != '-':
        while True:
            print("Incorrect answer!")
            turn = int(input(f"Position 1-9 ({x_or_o}): ")) - 1
            if table_list[turn] == '-':
                table_list[turn] = f'{x_or_o}'
                break
    else:
        table_list[turn] = f'{x_or_o}'


table()

while True:
    if game_over():
        print(game_over()[1])
        table_list = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
        print("Do you want to play a new game? (y/n)")
        answer = input()

        while answer not in ('y', 'n', 'Y', 'N'):
            print("Incorrect answer!")
            answer = input()

        if answer == 'y':
            table()
            continue
        elif answer == 'n':
            break

    turn_o = input("Position 1-9 (O): ")
    input_checker(turn_o, "O")
    table()

    if game_over():
        continue

    turn_x = input("Position 1-9 (X): ")
    input_checker(turn_x, "X")
    table()
