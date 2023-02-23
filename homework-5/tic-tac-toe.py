matrix = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]


def print_matrix(matrix):
    for row in matrix:
        for cell in row:
            print(cell, end=' ')
        print()


print_matrix(matrix)


def check_game_over(matrix):
    # Check if any row has three in a row
    for row in matrix:
        if row[0] != '-' and all(cell == row[0] for cell in row):
            return True, row[0]
    # Check if any column has three in a row
    for col in range(3):
        if matrix[0][col] != '-' and all(matrix[row][col] == matrix[0][col] for row in range(3)):
            return True, matrix[0][col]
    # Check if either diagonal has three in a row
    if matrix[0][0] != '-' and all(matrix[i][i] == matrix[0][0] for i in range(3)):
        return True, matrix[0][0]
    if matrix[0][2] != '-' and all(matrix[i][2-i] == matrix[0][2] for i in range(3)):
        return True, matrix[0][2]
    # Check if there are any empty cells left
    if any('-' in row for row in matrix):
        return False, None
    # If no one has won and there are no empty cells left, it's a tie
    return True, 'tie'


player1_turn = True

while True:
    if player1_turn:
        index_str = input("Player 1, please enter a row and column index, separated by a space: ")
        symbol = 'x'
    else:
        index_str = input("Player 2, please enter a row and column index, separated by a space: ")
        symbol = 'o'

    row, col = map(int, index_str.split())

    if matrix[row][col] != '-':
        print('There is already an item, try again.')
        continue

    matrix[row][col] = symbol
    print_matrix(matrix)

    game_over, winner = check_game_over(matrix)
    if game_over:
        if winner == 'tie':
            print("It's a tie!")
        else:
            print(f"{winner} has won!")
        break

    player1_turn = not player1_turn
