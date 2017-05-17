from grammar.grammarCVisitor import grammarCVisitor
from grammar.grammarCParser import grammarCParser
from symbolTable import symbolTable

class translate(grammarCVisitor):

    def __init__(self, sTable, filename):
        self.sTable = sTable
        end = filename.find('.c')
        filename = filename[:end]
        filename = filename[::-1]
        end = filename.find('/')
        if(end!=-1):
            filename = filename[:end]
        filename = filename[::-1]
        self.file = open(filename + '.p', 'w')

        self.T = {'pointer':'a', 'bool':'b', 'char':'c', 'int':'i', 'float':'r'}


    def visitMainFunc(self, ctx:grammarCParser.MainFuncContext):
        self.file.write("start:\n")
        self.visitChildren(ctx)

    def visitDeclaration(self, ctx:grammarCParser.DeclarationContext):
        t = ctx.types().getText()
        self.file.write("ldc " + str(self.T[t]) + " " + "0")

    #def visitDefinition(self, ctx:grammarCParser.DefinitionContext):
     #   pass
    def visitNormalAssignment(self, ctx:grammarCParser.NormalAssignmentContext):
        print(self.sTable.currentNode)
        t = self.sTable.search(ctx.lValue().getText())
        self.file.write("ldc ")