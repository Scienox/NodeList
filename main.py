from List import List
from Matrix import Matrix
import random
from demineur import Game

"""

"""


if __name__ == "__main__":
    #random.seed(0)
    game = Game(5, 5, 7)

    print(game.board)
    

    while True:
        row = int(input("Choice a row: "), )
        column = int(input("Choice a column: "))
        game.choice_case(row, column)
        print(game.board)
        print(game.reference_board)
