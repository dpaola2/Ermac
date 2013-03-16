#! /usr/bin/env python

import json
from ermac import Interpreter

def main():
    print "Reading lib/test_ast.json..."
    json_string = open("lib/test_ast.json").read()
    print "Parsing JSON..."
    ast = json.loads(json_string)
    print "Creating interpreter..."
    i = Interpreter(ast)
    print i
    
if __name__ == '__main__':
    main()
