class Matrix(object):

    matrix_string = []

    def __init__(self, matrix_string):
        self.matrix_string = matrix_string.split("\n")
        pass

    def row(self, index):
        return [int(item) for item in self.matrix_string[index].split(' ')]

    def column(self, index):
        return [int(item.split(' ')[index]) for item in self.matrix_string]