from random import randint
import re


def print_board(cells):
    print(f"""{'-' * 9}
| {cells[0]} {cells[1]} {cells[2]} |
| {cells[3]} {cells[4]} {cells[5]} |
| {cells[6]} {cells[7]} {cells[8]} |
{'-' * 9}""")


cells = '_' * 9
lines = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (6, 4, 2)
]
go = True

counter = 'X'

while go:

    # Stage 1: Ask for co-ordinates and validate the response
    while True:
        # Print the game board
        print_board(cells)

        # Ask player for co-ordinates
        [y_cor, x_cor] = (input('Enter the coordinates:')).split(' ')

        # Check if response is a digit
        if x_cor.isdigit() and y_cor.isdigit():
            x_cor = int(x_cor)
            y_cor = int(y_cor)
        else:
            print('You should enter numbers!')
            continue

        # Check if response is a co-ordinate on the board
        if x_cor not in range(1, 4) or y_cor not in range(1, 4):
            print("Coordinates should be from 1 to 3!")
            continue

        # Convert the coordinates to an Index number
        index = 4
        if x_cor == 1:
            if y_cor == 1:
                index = 6
            elif y_cor == 2:
                index = 7
            elif y_cor == 3:
                index = 8
        elif x_cor == 2:
            if y_cor == 1:
                index = 3
            elif y_cor == 2:
                index = 4
            elif y_cor == 3:
                index = 5
        elif x_cor == 3:
            if y_cor == 1:
                index = 0
            elif y_cor == 2:
                index = 1
            elif y_cor == 3:
                index = 2

        # Check if the player coordinates refer to an empty cell
        if cells[index] != '_':
            print(f'This cell is occupied! Choose another one!')
            continue

        break

    # Stage 2: Enter the entry onto the board and check if the game has been won

    # Enter the player's entry onto the board
    cells = cells[:index] + counter + cells[index + 1:]

    #  Harvest all the combinations of lines to check if one has won
    combinations = []
    for line in lines:
        combinations += [''.join(list(cells[i] for i in line))]

    # Get the number of entries, to make sure the board is legal later
    x_len = len([x for x in cells if x == 'X'])
    o_len = len([o for o in cells if o == 'O'])

    # Confirm if either player has won, or if the board is legal
    if x_len >= (o_len + 2) \
            or x_len <= (o_len - 2) \
            or 'XXX' in combinations and 'OOO' in combinations:
        print("Impossible")
    elif 'XXX' not in combinations and 'OOO' not in combinations:
        if not any(re.search('_', i) for i in combinations):
            print_board(cells)
            print("Draw")
            go = False
            break
    elif 'XXX' in combinations and 'OOO' not in combinations:
        print_board(cells)
        print("X wins")
        go = False
        break
    elif 'OOO' in combinations and 'XXX' not in combinations:
        print_board(cells)
        print("O wins")
        go = False
        break

    # Toggle counter for next player
    if counter == 'X':
        counter = 'O'
    else:
        counter = 'X'
