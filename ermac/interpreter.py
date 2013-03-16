
from nodes import *


class Interpreter:
    def __init__(self, ast):
        self.ast = ast # should be a dictionary
        self.root_key = ast[0]
        self.__dict__[self.root_key] = mapping[self.root_key](ast[1])

    def __str__(self):
        return "<Interpreter with root: %s>" % self.root_key
    
