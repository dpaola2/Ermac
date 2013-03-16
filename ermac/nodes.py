
from exceptions import NotImplementedError

def build_statements(statements):
    print "in build statements"
    new_statements = []
    for statement in statements:
        new_statement = Statement(statement)
    return new_statements

def evaluate(form):
    first_arg = form[0]
    rest_args = form[1:]
    func = mapping[first_arg]
    print "node = %s\t\tfirst_arg = %s\t\trest_args = %s" % (func, first_arg, rest_args)
    return mapping[first_arg](*rest_args)


class Atom:
    def __init__(self, atom):
        self.atom = atom
        print "creating atom %s" % atom

class Num:
    def __init__(self, num):
        self.num = num
        print "creating num %s" % num

class String:
    def __init__(self, string):
        self.string = string
        print "creating string %s" % string

class Name:
    def __init__(self, name):
        self.name = name
        print "creating name %s" % name

class Array:
    def __init__(self, elems):
        self.elems = elems
        print "creating array"

class Object:
    def __init__(self, properties):
        self.properties = []
        for prop in properties:
            name = prop[0]
            props = prop[1]
            value = evaluate(props)
            print "adding { %s : %s } to object properties" % (name, value)
            self.properties.append((name, value))
        
class Regexp:
    def __init__(self, expr, flags):
        self.expr = expr
        self.flags = flags

class Assign:
    def __init__(self, op, place, val):
        self.op = op
        self.place = place
        self.val = val
        print "inside Assign(%s, %s, %s)" % (op, place, val)

class Binary:
    def __init__(self, op, lhs, rhs):
        self.op = op
        self.lhs = lhs
        self.rhs = rhs

class UnaryPostfix:
    def __init__(self, op, place):
        self.op = op
        self.place = place

class UnaryPrefix:
    def __init__(self, op, place):
        self.op = op
        self.place = place

class Call:
    def __init__(self, func, args):
        self.func = func
        self.args = args

class Dot:
    def __init__(self, obj, attr):
        self.obj = obj
        self.attr = attr

class Sub:
    def __init__(self, obj, attr):
        self.obj = obj
        self.attr = attr

class Seq:
    def __init__(self, form1, result):
        self.form1 = form1
        self.result = result

class Conditional:
    def __init__(self, test, then, els):
        self.test = test
        self.then = then
        self.els = els

class Function:
    def __init__(self, name, args, statements):
        self.name = name
        self.args = args
        self.statements = []
        for s in statements:
            self.statements.append(evaluate(s))

        print "creating function: %s with arguments %s" % (name, args)
        print "\t and statements:"
        for s in self.statements:
            print "\t\t%s" % s

class New:
    def __init__(self, func, args):
        self.func = func
        self.args = args

class Toplevel:
    def __init__(self, statements):
        self.statements = build_statements(statements)
        print "creating toplevel with statements:"
        for s in self.statements:
            print "    %s" % s
            
class Block:
    def __init__(self, statements):
        self.statements = build_statements(statements)

class Statement:
    def __init__(self, form):
        first_arg = form[0]
        rest_args = form[1:]
        form = mapping[first_arg]
        self.form = form(*rest_args)

class Label:
    def __init__(self, name, form):
        self.name = name
        self.form = form

class If:
    def __init__(self, test, then, els):
        self.test = test
        self.then = then
        self.els = els
        print "creating if statement with:"
        print "    test: %s" % test
        print "    then: %s" % then
        print "    else: %s" % els


class With:
    def __init__(self, obj, body):
        self.obj = obj
        self.body = body

class Var:
    def __init__(self, bindings):
        self.bindings =[]
        for binding in bindings:
            name = binding[0]
            value = mapping[binding[1][0]](binding[1][1])
            print "creating var %s =  %s" % (name, value)
            self.bindings.append((name, value))

            
class Defun:
    def __init__(self, name, args, statements):
        self.name = name
        self.args = args
        self.statements = build_statements(statements)
        print "inside defun"

class Return:
    def __init__(self, value):
        self.value = value
        print "Return(%s)" % value

class Debugger:
    def __init__(self):
        pass

class Try:
    def __init__(self, body, catch, final):
        self.body = body
        self.catch = catch
        self.final = final

class Throw:
    def __init__(self, expr):
        self.expr = expr

class Break:
    def __init__(self, label):
        self.label = label

class Continue:
    def __init__(self, label):
        self.label = label

class While:
    def __init__(self, cond, body):
        self.cond = cond
        self.body = body

class Do:
    def __init__(self, cond, body):
        self.cond = cond
        self.body = body

class For:
    def __init__(self, init, cond, step, body):
        self.init = init
        self.cond = cond
        self.step = step
        self.body = body

class ForIn:
    def __init__(self, init, lhs, obj, body):
        self.init = init
        self.lhs = lhs
        self.obj = obj
        self.body = body

class Case:
    def __init__(self, case, body):
        self.case = case
        self.body = body

class Switch:
    def __init__(self, val, *cases):
        raise NotImplementError
        self.val = val
        self.cases = cases 

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
