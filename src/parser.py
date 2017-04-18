import sys
#sys.path.append('./grammar/')

from antlr4 import *
from grammar.grammarCLexer import grammarCLexer
from grammar.grammarCParser import grammarCParser



def main(argv):
    input = FileStream(argv[1])
    lexer = grammarCLexer(input)
    stream = CommonTokenStream(lexer)
    parser = grammarCParser(stream)
    tree = parser.program()

if __name__ == '__main__':
    main(sys.argv)