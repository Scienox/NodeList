from Matrix import Matrix
from List import List
import random


class Game:
    def __init__(self, row, column, bombs):
        self.reference_board = Matrix(row, column)
        self.bombs = bombs
        self.is_playing = False

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

        for _row, _column in self.get_neighbors_coordonates(row, column):
            neighbor_list.pushAfter(self.reference_board[_row][_column])

        return neighbor_list

    def get_neighbors_coordonates(self, row, column):
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
            top = (row-1, column)
            neighbor_list.pushAfter(top)
            if column > 0:
                topLeft = (row-1, column-1)
                neighbor_list.pushAfter(topLeft)
            if column < column_max:
                topRight = (row-1, column+1)
                neighbor_list.pushAfter(topRight)

        if column > 0:
            left = (row, column-1)
            neighbor_list.pushAfter(left)
        if column < column_max:
            right = (row, column+1)
            neighbor_list.pushAfter(right)

        if row < row_max:
            bottom = (row+1, column)
            neighbor_list.pushAfter(bottom)
            if column > 0:
                bottomLeft = (row+1, column-1)
                neighbor_list.pushAfter(bottomLeft)
            if column < column_max:
                bottomRight = (row+1, column+1)
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

    def foreach(self, matrix):
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                yield matrix[row][column]

    def check_loose(self, target):
        row, column = target
        if self.board[row][column] == "X":
            print("You loose!")
            return True
        return False

    def safe_cases_discovered(self) -> tuple:
        safe_cases = 0
        bombs_founded = 0
        for row in range(len(self.board)):
            for column in range(len(self.board[0])):
                if self.board[row][column] == ("." or "F"):
                    safe_cases += 1
                if (self.board[row][column] == "F") and (self.reference_board[row][column] == "X"):
                    bombs_founded += 1
                elif (self.board[row][column] == "F") and (self.reference_board[row][column] != "X"):
                    return 0, 0
        return safe_cases, bombs_founded

    def check_win(self):
        safe_cases, bombs_founded = self.safe_cases_discovered()
        bombs_missed = self.bombs == safe_cases
        bombs__founded = self.bombs == bombs_founded
        
        if bombs__founded or bombs_missed:
            print("You Win!")
            return True
        return False

    def choice_case(self, row, column, action):
        if not self.is_playing:
            self.is_playing = True
            self.place_bombs((row, column))
            self.detect_bombs_per_case()
            #self.board[row][column] = self.reference_board[row][column]
            self.show(row, column)
        else:

            if action.upper() == "F" and self.board[row][column] == "F":
                self.board[row][column] = "."
            elif action.upper() == "F" and self.board[row][column] == ".":
                self.board[row][column] = "F"
            else:
                self.show(row, column)

    def show_recursive(self, neighbors):
        for row, column in neighbors:
            coordonate = (row, column)
            content = self.reference_board[row][column]
            if isinstance(content, int) and content == 0:
                neighbors_iter = self.get_neighbors_coordonates(row, column)

                for _row, _column in neighbors_iter:
                    _coordonate = (_row, _column)
                    if (_coordonate not in neighbors):
                        neighbors.pushAfter(_coordonate)

        return neighbors

    def show(self, row, column):
        content = self.reference_board[row][column]
        discover = List()
        discover.pushAfter((row, column))
        if isinstance(content, int) and (content == 0):
            discover = self.show_recursive(discover)
        for _row, _column in discover:
            self.board[_row][_column] = self.reference_board[_row][_column]


    def start(self):
        print(self.board)

        while True:
            row = int(input("Choice a row: "), )
            column = int(input("Choice a column: "))
            action = input("Action: empty=discover, set_falg=f, remove_flag=f:\n-> ")
            self.choice_case(row, column, action)
            print(self.board)
            print(self.reference_board)  # show cheat
            if self.check_win() or self.check_loose((row, column)):
                break
