import sys

table = [
    '-', '-', '-',
    '-', '-', '-',
    '-', '-', '-'
]


def print_table():
    print(f"{table[0]} | {table[1]} | {table[2]}")
    print(f"{table[3]} | {table[4]} | {table[5]}")
    print(f"{table[6]} | {table[7]} | {table[8]}")


def is_win(items):
    if all(item == items[0] for item in items) and '-' not in items:
        return True


def is_game_over():
    # Horizontal
    if is_win((table[0], table[1], table[2])):
        return True
    elif is_win((table[3], table[4], table[5])):
        return True
    elif is_win((table[6], table[7], table[8])):
        return True

    # Vertical
    elif is_win((table[0], table[3], table[6])):
        return True
    elif is_win((table[1], table[4], table[7])):
        return True
    elif is_win((table[2], table[5], table[8])):
        return True

    # Diagonals
    elif is_win((table[0], table[4], table[8])):
        return True
    elif is_win((table[2], table[4], table[6])):
        return True

    if '-' not in table:
        print('Match Draw!')
        handle_game_over()


def handle_game_over():
    global table
    table = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

    valid_answers = ('y', 'Y', 'n', 'N')

    while True:
        answer = input('Do you want to play a new game? (y/n): ')
        if answer in valid_answers:
            break

        print('Invalid answer!')

    if answer == 'y' or answer == 'Y':
        game()
    else:
        sys.exit()


def make_turn(player):
    valid_numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9')

    while True:
        turn = input(f"Position 1-9 ({player}): ")
        if turn.isdigit() and turn in valid_numbers and table[int(turn) - 1] == '-':
            break

        print('Invalid input!')

    table[int(turn) - 1] = player
    print_table()

    if is_game_over():
        print(f"Player ({player}) wins the game!")
        handle_game_over()


def game():
    while True:
        make_turn('O')
        make_turn('X')


game()
