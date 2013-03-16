
from nodes import *

mapping = {
    'atom': Atom,
    'num': Num,
    'string': String,
    'name': Name,
    'array': Array,
    'object': Object,
    'regexp': Regexp,
    'assign': Assign,
    'binary': Binary,
    'unary-postfix': UnaryPostfix,
    'unary-prefix': UnaryPrefix,
    'call': Call,
    'dot': Dot,
    'sub': Sub,
    'seq': Seq,
    'conditional': Conditional,
    'function': Function,
    'new': New,
    'toplevel': Toplevel,
    'block': Block,
    'stat': Statement,
    'label': Label,
    'if': If,
    'with': With,
    'var': Var,
    'defun': Defun,
    'return': Return,
    'debugger': Debugger,
    'try': Try,
    'throw': Throw,
    'break': Break,
    'continue': Continue,
    'while': While,
    'do': Do,
    'for': For,
    'for-in': ForIn,
    'switch': Switch
    }

class Interpreter:
    def __init__(self, ast):
        self.ast = ast # should be a dictionary

