table_list = ['-', '-', '-',
              '-', '-', '-',
              '-', '-', '-']


def table():
    print(table_list[0] + "|" + table_list[1] + "|" + table_list[2])
    print(table_list[3] + "|" + table_list[4] + "|" + table_list[5])
    print(table_list[6] + "|" + table_list[7] + "|" + table_list[8])


def check_if_win():
    if table_list[0] != '-' and table_list[4] != '-' and table_list[8] != '-' and table_list[0] == table_list[4] and table_list[4] == table_list[8]:
        return True, table_list[0]
    elif table_list[6] != '-' and table_list[4] != '-' and table_list[2] != '-' and table_list[6] == table_list[4] and table_list[4] == table_list[2]:
        return True, table_list[6]
    elif table_list[0] != '-' and table_list[3] != '-' and table_list[6] != '-' and table_list[0] == table_list[3] and table_list[3] == table_list[4]:
        return True, table_list[0]
    elif table_list[1] != '-' and table_list[4] != '-' and table_list[7] != '-' and table_list[1] == table_list[4] and table_list[4] == table_list[7]:
        return True, table_list[1]
    elif table_list[2] != '-' and table_list[5] != '-' and table_list[8] != '-' and table_list[2] == table_list[5] and table_list[5] == table_list[8]:
        return True, table_list[2]
    elif table_list[0] != '-' and table_list[1] != '-' and table_list[2] != '-' and table_list[0] == table_list[1] and table_list[1] == table_list[2]:
        return True, table_list[0]
    elif table_list[3] != '-' and table_list[4] != '-' and table_list[5] != '-' and table_list[3] == table_list[4] and table_list[4] == table_list[5]:
        return True, table_list[3]
    elif table_list[6] != '-' and table_list[7] != '-' and table_list[8] != '-' and table_list[6] == table_list[7] and table_list[7] == table_list[8]:
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


def o_turn():
    turn_o = input("Position 1-9 (O): ")

    # checks for input problems
    is_digit = turn_o.isnumeric()
    while not is_digit:
        print("Incorrect answer!")
        turn_o = input("Position 1-9 (O): ")
        is_digit = turn_o.isnumeric()
    turn_o = int(turn_o) - 1

    while turn_o + 1 not in one_to_nine:
        print("Incorrect answer!")
        turn_o = int(input("Position 1-9 (O): ")) - 1

    if table_list[turn_o] != '-':
        while True:
            print("Incorrect answer!")
            turn_o = int(input("Position 1-9 (O): ")) - 1
            if table_list[turn_o] == '-':
                table_list[turn_o] = 'O'
                break
    else:
        table_list[turn_o] = 'O'


def x_turn():
    turn_x = input("Position 1-9 (X): ")

    # checks for input problems
    is_digit = turn_x.isnumeric()
    while not is_digit:
        print("Incorrect answer!")
        turn_x = input("Position 1-9 (X): ")
        is_digit = turn_x.isnumeric()
    turn_x = int(turn_x) - 1

    while turn_x + 1 not in one_to_nine:
        print("Incorrect answer!")
        turn_x = int(input("Position 1-9 (X): ")) - 1

    if table_list[turn_x] != '-':
        while True:
            print("Incorrect answer!")
            turn_x = int(input("Position 1-9 (X): ")) - 1
            if table_list[turn_x] == '-':
                table_list[turn_x] = 'X'
                break
    else:
        table_list[turn_x] = 'X'


table()

while True:
    if game_over():
        print(game_over()[1])
        table_list = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
        print("Do you want to play a new game? (y/n)")
        answer = input()

        while answer != 'y' and answer != 'n':
            print("Incorrect answer!")
            answer = input()

        if answer == 'y':
            table()
            continue
        elif answer == 'n':
            break

    o_turn()
    table()

    if game_over():
        continue

    x_turn()
    table()
