from grammar.grammarCVisitor import grammarCVisitor
from grammar.grammarCParser import grammarCParser
from symbolTable import symbolTable

class buildSymbolTable(GrammarCVisitor):

    def __init__(self, parser):
        self.parser = parser
        self.symbol_Table = symbolTable()

    def visitProgram(self, ctx:grammarCParser.ProgramContext):
        self.symbol_Table.addChild("Program")
        self.visitChildren(ctx)
        self.goToParent()

    def visitMain(self, ctx:grammarCParser.MainFuncContext):
        self.symbol_Table.add("Main", "mainfunction", ctx.getChild(0).getText())
        self.symbol_Table.addChild("Main")
        self.visitChildren(ctx)
        self.symbol_Table.goToParent()

    def visitFuncDef(self, ctx:grammarCParser.FuncDefContext):
        name = self.visitLValue(ctx.LValue())
        self.symbol_Table.add(name, "function definition", self.visitTypes(ctx.types()))
        self.symbol_Table.addChild(name)
        self.visitChildren(ctx)
        self.symbol_Table.goToParent()

    def visitTypes(self, ctx:grammarCParser.TypesContext):
        return ctx.getText()

    def visitArgList(self, ctx:grammarCParser.ArgListContext):
        if(ctx.getChildCount()!=0):
            typeList = ctx.types()
            idList = ctx.lValue()
            if(len(typeList)==len(idList)):
                for i in range(len(typeList)):
                    self.add(idList[i], "function argument", typeList[i])


    def visitBody(self, ctx:grammarCParser.BodyContext):
        self.symbol_Table.add

    def visitLValue(self, ctx:grammarCParser.LValueContext):
        return ctx.getText()