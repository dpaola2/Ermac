
from exceptions import NotImplementedError

class Atom:
    def __init__(self, atom):
        self.atom = atom
        print self
        
    def __str__(self):
        return "<Atom %s>" % self.atom

class Num:
    def __init__(self, num):
        self.num = num
        print self
        
    def __str__(self):
        return "<Num %s>" % self.num

class String:
    def __init__(self, string):
        self.string = string
        print self
        
    def __str__(self):
        return "<String %s>" % self.string

class Name:
    def __init__(self, name):
        self.name = name
        print self
        
    def __str__(self):
        return "<Name %s>" % self.name

class Array:
    def __init__(self, elems):
        self.elems = elems
        print self
        
    def __str__(self):
        return "<Array %s>" % self.elems

class Object:
    def __init__(self, properties):
        self.properties = {}
        for prop in properties:
            name = prop[0]
            props = prop[1]
            value = evaluate(props)
            self.properties[name] = value
        print self

    def __str__(self):
        return "<Object %s>" % self.properties
        
class Regexp:
    def __init__(self, expr, flags):
        self.expr = expr
        self.flags = flags
        print self

    def __str__(self):
        return "<Regexp expr: %s flags: %s>" % (self.expr, self.flags)

class Assign:
    def __init__(self, op, place, val):
        self.op = op
        self.place = place
        self.val = val
        print self

    def __str__(self):
        return "<Assign op: %s, place: %s, val: %s>" % (self.op, self.place, self.val)

class Binary:
    def __init__(self, op, lhs, rhs):
        self.op = op
        self.lhs = evaluate(lhs)
        self.rhs = evaluate(rhs)
        print self

    def __str__(self):
        return "<Binary op: %s lhs: %s rhs: %s>" % (self.op, self.lhs, self.rhs)

class UnaryPostfix:
    def __init__(self, op, place):
        self.op = op
        self.place = place
        print self

    def __str__(self):
        return "<UnaryPostfix op: %s place: %s>" % (self.op, self.place)
        

class UnaryPrefix:
    def __init__(self, op, place):
        self.op = op
        self.place = place
        print self

    def __str__(self):
        return "<UnaryPrefix op: %s place: %s>" % (self.op, self.place)

class Call:
    def __init__(self, func, args):
        self.func = func
        self.args = args
        print self

    def __str__(self):
        return "<Call function: %s args: %s>" % (self.func, self.args)
        
class Dot:
    def __init__(self, obj, attr):
        self.obj = obj
        self.attr = attr
        print self

    def __str__(self):
        return "<Dot obj: %s attr: %s>" % (self.obj, self.attr)

class Sub:
    def __init__(self, obj, attr):
        self.obj = obj
        self.attr = attr
        print self

    def __str__(self):
        return "<Sub obj: %s attr: %s>" % (self.obj, self.attr)

class Seq:
    def __init__(self, form1, result):
        self.form1 = form1
        self.result = result
        print self

    def __str__(self):
        return "<Seq form1: %s result: %s>" % (self.form1, self.result)

class Conditional:
    def __init__(self, test, then, els):
        self.test = evaluate(test)
        self.then = evaluate(then)
        if els is None:
            self.els = None
        self.els = evaluate(els)
        print self

    def __str__(self):
        return "<Conditional %s %s %s>" % (self.test, self.then, self.els)

class Function:
    def __init__(self, name, args, statements):
        self.name = name
        self.args = [evaluate(arg) for arg in args]
        self.statements = [evaluate(s) for s in statements]
        print self

    def __str__(self):
        return "<Function name: %s args: %s statements: %s>" % (self.name, self.args, self.statements)

class New:
    def __init__(self, func, args):
        self.func = func
        self.args = args
        print self

    def __str__(self):
        return "<New func: %s args: %s>" % (self.func, self.args)

class Toplevel:
    def __init__(self, statements):
        self.statements = [evaluate(s) for s in statements]
        print self

    def __str__(self):
        return "<Toplevel %s statements: %s>" % (len(self.statements), self.statements)
            
class Block:
    def __init__(self, statements):
        self.statements = [Statement(s) for s in statements]
        print self

    def __str__(self):
        return "<Block %s statements: %s>" % (len(self.statements), self.statements)

class Statement:
    def __init__(self, form):
        self.form = evaluate(form)
        print self

    def __str__(self):
        return "<Statement %s>" % self.form

class Label:
    def __init__(self, name, form):
        self.name = name
        self.form = form
        print self

    def __str__(self):
        return "<Label %: %s>" % (self.name, self.form)

class If:
    def __init__(self, test, then, els):
        self.test = evaluate(test)
        self.then = evaluate(then)
        if els is None:
            self.els = els
        else:
            self.els = evaluate(els)
        print self

    def __str__(self):
        return "<If %s %s %s>" % (self.test, self.then, self.els)

class With:
    def __init__(self, obj, body):
        self.obj = obj
        self.body = body
        print self

    def __str__(self):
        return "<With obj: %s body: %s>" % (self.obj, self.body)

class Var:
    def __init__(self, bindings):
        self.bindings = {}
        for binding in bindings:
            name = binding[0]
            value = evaluate(binding[1])
            self.bindings[name] = value
        print self

    def __str__(self):
        return "<Var %s>" % self.bindings

            
class Defun:
    def __init__(self, name, args, statements):
        self.name = name
        self.args = args
        self.statements = [Statement(s) for s in statements]
        print "inside defun"

class Return:
    def __init__(self, value):
        self.value = evaluate(value)
        print self

    def __str__(self):
        return "<Return %s>" % self.value

class Debugger:
    def __init__(self):
        print self

    def __str__(self):
        return "<Debugger>"

class Try:
    def __init__(self, body, catch, final):
        self.body = body
        self.catch = catch
        if final is None:
            self.final = None
        else:
            self.final = final
        print self

    def __str__(self):
        return "<Try %s %s %s>" % (self.body, self.catch, self.final)

class Throw:
    def __init__(self, expr):
        if expr is None:
            self.expr = None
        else:
            self.expr = evaluate(expr)
        print self

    def __str__(self):
        return "<Throw %s>" % self.expr

class Break:
    def __init__(self, label):
        self.label = label
        print self

    def __str__(self):
        return "<Break %s>" % self.label
    
class Continue:
    def __init__(self, label):
        self.label = label
        print self

    def __str__(self):
        return "<Continue %s>" % self.label

class While:
    def __init__(self, cond, body):
        self.cond = evaluate(cond)
        self.body = evaluate(body)
        print self

    def __str__(self):
        return "<While %s %s>" % (self.cond, self.body)

class Do:
    def __init__(self, cond, body):
        self.cond = evaluate(cond)
        self.body = evaluate(body)
        print self

    def __str__(self):
        return "<Do %s %s>" % (self.cond, self.body)

class For:
    def __init__(self, init, cond, step, body):
        self.init = evaluate(init)
        self.cond = evaluate(cond)
        self.step = step
        self.body = evaluate(body)
        print self

    def __str__(self):
        return "<For init: %s cond: %s step: %s body: %s>" % (self.init, self.cond, self.step, self.body)

class ForIn:
    def __init__(self, init, lhs, obj, body):
        self.init = evaluate(init)
        self.lhs = lhs
        self.obj = obj
        self.body = evaluate(body)
        print self

    def __str__(self):
        return "<ForIn init: %s lhs: %s obj: %s body: %s>" % (self.init, self.lhs, self.obj, self.body)

class Case:
    def __init__(self, case, body):
        self.case = case
        self.body = evaluate(body)
        print self

    def __str__(self):
        return "<Case %s body: %s>" % (self.case, self.body)

class Switch:
    def __init__(self, val, *cases):
        self.val = val
        self.cases = cases
        print self

    def __str__(self):
        return "<Switch %s %s>" % (self.val, self.cases)

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

def evaluate(form):
    print "------> evaluating %s" % form
    first_arg = form[0]
    rest_args = form[1:]
    func = mapping[first_arg]
    return mapping[first_arg](*rest_args)
