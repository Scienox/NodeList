from List import List
from Matrix import Matrix
import random
from demineur import Game

"""

"""


def select_case(matrix, nbomb):
    selection = List()
    tmpCaseAvaible = matrix.copy()
    for bomb in range(nbomb):
        row = len(tmpCaseAvaible) - 1
        column = len(tmpCaseAvaible[0]) - 1
        coordonate = (random.randint(0, row), random.randint(0, column))

        tmpCaseAvaible[coordonate[0]].pop(coordonate[1])

        if len(tmpCaseAvaible[coordonate[0]]) < 1:
            tmpCaseAvaible.pop(coordonate[0])

        selection.pushAfter(coordonate)
    return selection

def get_neighbor(row, column, board):
    neighbor_list = List()
    """
    top
    topLeft
    topRight
    left
    right
    bottom
    bottomLeft
    bottomRight
    """
    row_max = len(board[0]) - 1
    column_max = len(board) - 1

    if row > 0:
        top = board[row-1][column]
        neighbor_list.pushAfter(top)
        if column > 0:
            topLeft = board[row-1][column-1]
            neighbor_list.pushAfter(topLeft)
        if column < column_max:
            topRight = board[row-1][column+1]
            neighbor_list.pushAfter(topRight)

    if column > 0:
        left = board[row][column-1]
        neighbor_list.pushAfter(left)
    if column < column_max:
        right = board[row][column+1]
        neighbor_list.pushAfter(right)


    if row < row_max:
        bottom = board[row+1][column]
        neighbor_list.pushAfter(bottom)
        if column > 0:
            bottomLeft = board[row+1][column-1]
            neighbor_list.pushAfter(bottomLeft)
        if column < column_max:
            bottomRight = board[row+1][column+1]
            neighbor_list.pushAfter(bottomRight)

    return neighbor_list


def place_bomb(matrix, selection):
    for coordonate in selection:
        row = coordonate[0]
        column = coordonate[1]
        matrix[row][column] = "X"


if __name__ == "__main__":
    """random.seed(0)
    board = Matrix(5, 5)
    print(board)
    selection = select_case(board, 7)
    place_bomb(board, selection)
    print(board)

    print(get_neighbor(0, 1, board))"""
    random.seed(0)
    game = Game(5, 5, 7)

    print(game.get_neighbors(1, 4))
