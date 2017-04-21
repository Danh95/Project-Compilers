from grammar.grammarCVisitor import grammarCVisitor

class buildAST(grammarCVisitor):

    def __init__(self, parser):
        self.parser = parser

    def visitProgram(self, ctx:grammarCParser.ProgramContext):
        programctx = self.parser.ProgramContext()
        print("Programnode")
        return self.visitChildren(ctx)
    def toDot(self):