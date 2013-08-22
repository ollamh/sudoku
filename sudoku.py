# encoding: utf-8
import numpy as np
import random

# TODO: move to utils
def generate_seed_matrix(matrix_size=3, numbers=9):
    """
    Generates seed matrix for sudoku generator
    :param matrix_size - size of generated matrix, by default 3
    :param numbers - upper limit of numbers' range for generator, default 9
    :output - string for numpy matrix (spaces are column separators and
    semicolons are row separators)
    """
    field = range(1,numbers+1)
    res = ""
    while field:
        ch = random.choice(field)
        field.remove(ch)
        res += "{0}{1}".format(ch, " " if len(field) % 3 else ";")
    return res[:-1]

class Sudoku(object):

    def __init__(self, *args, **kwargs):
        self.size = kwargs.pop('size', 9)
        self.generate()

    def __unicode__(self):
        return u'Sudoku {0}x{0}'.format(self.size)

    def __str__(self):
        pass

    def generate(self):
        """
        Main sudoku rules:
         - no repeating numbers in one row
         - no repeating numbers in one column
         - no repeating numbers in local group of cells 3x3
        """
        self.B1 = np.matrix(generate_seed_matrix(3, self.size))
        self.B2 = np.dot([[0,0,1],[1,0,0],[0,1,0]], self.B1)
        self.B3 = np.dot([[0,1,0],[0,0,1],[1,0,0]], self.B1)
        self.B4 = np.dot(self.B1, [[0,1,0],[0,0,1],[1,0,0]])
        self.B5 = np.dot([[0,0,1],[1,0,0],[0,1,0]], self.B4)
        self.B6 = np.dot(self.B3, [[0,0,1],[1,0,0],[0,1,0]])
        self.B7 = np.dot(self.B1, [[0,0,1],[1,0,0],[0,1,0]])
        self.B8 = np.dot(self.B2, [[0,0,1],[1,0,0],[0,1,0]])
        self.B9 = np.dot(self.B3, [[0,1,0],[0,0,1],[1,0,0]])
        self.U1 = np.hstack((self.B1, self.B2, self.B3))
        self.U2 = np.hstack((self.B4, self.B5, self.B6))
        self.U3 = np.hstack((self.B7, self.B8, self.B9))
        self.U = np.vstack((self.U1, self.U2, self.U3))
        print self.U
