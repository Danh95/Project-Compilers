import sys
#sys.path.append('./grammar/')

from antlr4 import *
from grammar.grammarCLexer import grammarCLexer
from grammar.grammarCParser import grammarCParser
from grammar.grammarCVisitor import grammarCVisitor
from buildAST import buildAST
from buildSymbolTable import buildSymbolTable
from translate import translate

"""def make_AST(st, ctx):
    syntaxtree = grammarCVisitor(st)
    syntaxtree.visitProgram(ctx.programContex())
"""
def main(argv):
    input = FileStream(argv[1])
    lexer = grammarCLexer(input)
    stream = CommonTokenStream(lexer)
    parser = grammarCParser(stream)
    tree = parser.program()
    #AST = buildAST(parser)
    #AST.visitProgram(tree)
    Symbol_Table = buildSymbolTable(parser, argv[1])
    Symbol_Table.visitProgram(tree)


if __name__ == '__main__':
    main(sys.argv)