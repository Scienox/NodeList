from Matrix import Matrix
from List import List
import random


class Game:
    def __init__(self, row, column, bombs):
        self.reference_board = Matrix(row, column)
        self.bombs = bombs
        self.start = False

        #self.place_bombs()
        #self.detect_bombs_per_case()

        self.board = self.reference_board.copy()
        for row in range(len(self.board)):
            for column in range(len(self.board[0])):
                self.board[row][column] = '.'

    def select_cases(self, nbomb, startCase):
        selection = List()
        tmpCaseAvaible = List()

        for row in range(len(self.reference_board)):
            for column in range(len(self.reference_board[row])):
                if (row, column) != startCase:
                    tmpCaseAvaible.pushAfter((row, column))

        for bomb in range(nbomb):
            fingerDeath = random.randint(0, len(tmpCaseAvaible) - 1)

            coordonate = tmpCaseAvaible.pop(fingerDeath)

            selection.pushAfter(coordonate)

        return selection

    def get_neighbors(self, row, column):
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
        row_max = len(self.reference_board[0]) - 1
        column_max = len(self.reference_board) - 1

        if row > 0:
            top = self.reference_board[row-1][column]
            neighbor_list.pushAfter(top)
            if column > 0:
                topLeft = self.reference_board[row-1][column-1]
                neighbor_list.pushAfter(topLeft)
            if column < column_max:
                topRight = self.reference_board[row-1][column+1]
                neighbor_list.pushAfter(topRight)

        if column > 0:
            left = self.reference_board[row][column-1]
            neighbor_list.pushAfter(left)
        if column < column_max:
            right = self.reference_board[row][column+1]
            neighbor_list.pushAfter(right)

        if row < row_max:
            bottom = self.reference_board[row+1][column]
            neighbor_list.pushAfter(bottom)
            if column > 0:
                bottomLeft = self.reference_board[row+1][column-1]
                neighbor_list.pushAfter(bottomLeft)
            if column < column_max:
                bottomRight = self.reference_board[row+1][column+1]
                neighbor_list.pushAfter(bottomRight)

        return neighbor_list

    def count_bombs(self, row, column):
        count = 0
        neighbors = self.get_neighbors(row, column)
        for case in neighbors:
            if str(case) == "X":
                count += 1
        return count

    def detect_bombs_per_case(self):
        for row in range(len(self.reference_board)):
            for column in range(len(self.reference_board[row])):
                bombs_detected = self.count_bombs(row, column)
                if self.reference_board[row][column] != "X":
                    self.reference_board[row][column] = bombs_detected

    def place_bombs(self, startCase):
        selection = self.select_cases(self.bombs, startCase)
        for coordonate in selection:
            row = coordonate[0]
            column = coordonate[1]
            self.reference_board[row][column] = "X"

        self.count_bombs

    def choice_case(self, row, column):
        if not self.start:
            self.start = True
            self.place_bombs((row, column))
            self.detect_bombs_per_case()
        
        self.board[row][column] = self.reference_board[row][column]
