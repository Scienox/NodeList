from List import List

class Matrix(List):
    """
    Square matrix
    """
    def __init__(self, row=0, column=0):
        super().__init__()
        for _ in range(row):
            new_row = List()
            for _ in range(column):
                new_row.pushAfter(None)
            self.pushAfter(new_row)
    
    def __str__(self):
        board = ""
        for row in range(len(self)):
            board += "(" + " | ".join(str(element) for element in self[row]) + ")\n"
        return board

    def copy(self):
        tmp = Matrix()
        for element in self:
            tmp.pushAfter(element)
        return tmp

    def reverse(self, direction:"vertical, orthogonal"="vertical"):
        tmp = Matrix()
        if direction == "vertical":
            for element in reversed(self):
                tmp.pushAfter(element)
        else:
            tmp = Matrix(len(self), len(self[0]))
            for row in range(len(self)):
                for column in range(len(self[0])-1, -1, -1):
                    tmp[row][len(self[row]) - column - 1] = self[row][column]
        return tmp

    def show_elements_per_cordonate(self):
        for row in range(len(self)):
            for column in range(len(self[row])):
                yield f"({row}, {column}) = " + str(self[row][column])
