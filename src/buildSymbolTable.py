from grammar.grammarCVisitor import grammarCVisitor
from grammar.grammarCParser import grammarCParser
from symbolTable import symbolTable

class buildSymbolTable(grammarCVisitor):

    def __init__(self, parser):
        self.parser = parser
        self.symbol_Table = symbolTable()

    def visitProgram(self, ctx:grammarCParser.ProgramContext):
        self.symbol_Table.addChild("Program")
        self.visitChildren(ctx)
        self.symbol_Table.goToParent()


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

    def visitFuncDecl(self, ctx:grammarCParser.FuncDeclContext):
        name = self.visitLValue(ctx.LValue())
        self.symbol_Table.add(name, "function declaration", self.visitTypes(ctx.types()))
        self.symbol_Table.addChild(name)
        self.visitChildren(ctx)
        self.symbol_Table.goToParent()

    def visitTypes(self, ctx:grammarCParser.TypesContext):
        return ctx.getText()

    def visitArgList(self, ctx:grammarCParser.ArgListContext):
        if(ctx.getChildCount()!=0):
            typeList = ctx.types()
            idList = ctx.lValue()
                #get types and var_name list
                #index of both list correspond
            if(len(typeList)==len(idList)):
                for i in range(len(typeList)):
                    #put the right duo in the symbol table
                    self.add(idList[i], "function argument", typeList[i])


    def visitDeclaration(self, ctx:grammarCParser.DeclarationContext):
        name = self.visitLValue(ctx.lValue())
        self.symbol_Table.add(name, "var declaration", self.visitTypes(ctx.types()))

    def visitDefinition(self, ctx:grammarCParser.DefinitionContext):
        name = self.visitAssignment(ctx.assignment())
        self.symbol_Table.add(name, "var definition", self.visitTypes(ctx.types()))

    def visitNormalAssignment(self, ctx:grammarCParser.NormalAssignmentContext):
        return self.visitLValue(ctx.lValue())

    def visitArrayAssignment(self, ctx:grammarCParser.ArrayAssignmentContext):
        return ctx.visitLValue()

    def visitIfStatement(self, ctx:grammarCParser.IfStatementContext):
        self.symbol_Table.addChild("if")
        self.visitBody(ctx.body())
        self.symbol_Table.goToParent()

    def visitElifStatement(self, ctx:grammarCParser.ElifStatementContext):
        self.symbol_Table.addChild("else if")
        self.visitBody(ctx.body())
        self.symbol_Table.goToParent()

    def visitElseStatement(self, ctx:grammarCParser.ElseStatementContext):
        self.symbol_Table.addChild("else")
        self.visitBody(ctx.body())
        self.symbol_Table.goToParent()

    def visitWhileStatement(self, ctx:grammarCParser.WhileStatementContext):
        self.symbol_Table.addChild("while")
        self.visitBody(ctx.body())
        self.symbol_Table.goToParent()

    def visitLoop(self, ctx:grammarCParser.WhileStatementContext):
        self.symbol_Table.addChild("if")
        self.visitForCondition(ctx.forCondition())
        self.visitBody(ctx.body())
        self.symbol_Table.goToParent()



    def visitLValue(self, ctx:grammarCParser.LValueContext):
        return ctx.getText()
        
