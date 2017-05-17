from grammar.grammarCVisitor import grammarCVisitor
from grammar.grammarCParser import grammarCParser
from symbolTable import symbolTable
import sys

class buildSymbolTable(grammarCVisitor):

    def __init__(self, parser):
        self.parser = parser
        self.symbol_Table = symbolTable()
        self.SP = 0

    def visitProgram(self, ctx:grammarCParser.ProgramContext):
        self.symbol_Table.addChild("Program")
        self.visitChildren(ctx)
        self.symbol_Table.goToParent()

    def visitMainFunc(self, ctx:grammarCParser.MainFuncContext):
        self.symbol_Table.add("Main", "mainfunction", ctx.getChild(0).getText())
        self.symbol_Table.addChild("Main")
        self.visitChildren(ctx)
        self.symbol_Table.goToParent()

    def visitFuncDef(self, ctx:grammarCParser.FuncDefContext):
        name = self.visitLValue(ctx.lValue())
        self.symbol_Table.add(name, "function definition", self.visitTypes(ctx.types()))
        self.symbol_Table.addChild(name)
        self.visitChildren(ctx)
        self.symbol_Table.goToParent()

    def visitFuncDecl(self, ctx:grammarCParser.FuncDeclContext):
        name = self.visitLValue(ctx.lValue())
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
                    self.symbol_Table.add(idList[i].getText(), "function argument", typeList[i].getText(), self.SP)
                    self.SP

    def visitDeclaration(self, ctx:grammarCParser.DeclarationContext):
        name = self.visitLValue(ctx.lValue())
        if(self.symbol_Table.search(ctx.lValue().getText())!=False):
            print("Error: Redeclaration of " + ctx.lValue().getText())
            sys.exit()
        self.symbol_Table.add(name, "var declaration", self.visitTypes(ctx.types()), self.SP)
        self.SP += 1

    def visitDefinition(self, ctx:grammarCParser.DefinitionContext):
        name = ctx.assignment().normalAssignment().lValue().getText()
        if(self.symbol_Table.search(name)!=False):
            print("Error: Redefinition of " + name)
            sys.exit()
        self.symbol_Table.add(name, "var definition", self.visitTypes(ctx.types()), self.SP)
        self.SP += 1
        self.visitAssignment(ctx.assignment())

    def visitFunctionCall(self, ctx:grammarCParser.FunctionCallContext):
        if(self.symbol_Table.search(self.visitLValue(ctx.lValue()))==False):
            print("Error: Function called before definition, unvalid reference to " + ctx.lValue().getText())
            sys.exit()

    def visitNormalAssignment(self, ctx:grammarCParser.NormalAssignmentContext):
        self.symbol_Table.resetType()
        if(self.symbol_Table.search(ctx.lValue().getText())==False):
            print("Error: Assignment before declaration, unvalid reference to " + ctx.lValue().getText())
            sys.exit()
        self.visitChildren(ctx)

    def visitArrayAssignment(self, ctx:grammarCParser.ArrayAssignmentContext):

        if(self.symbol_Table.search(ctx.lValue().getText())==False):
            print("Error: Assignment before declaration, invalid reference to " + ctx.lValue().getText())
            sys.exit()
        self.visitChildren(ctx)

    def visitIfStatement(self, ctx:grammarCParser.IfStatementContext):
        self.symbol_Table.addChild("if")
        self.visitCondition(ctx.condition())
        self.visitBody(ctx.body())
        self.symbol_Table.goToParent()

    def visitElifStatement(self, ctx:grammarCParser.ElifStatementContext):
        self.symbol_Table.addChild("else if")
        self.visitCondition(ctx.condition())
        self.visitBody(ctx.body())
        self.symbol_Table.goToParent()

    def visitElseStatement(self, ctx:grammarCParser.ElseStatementContext):
        self.symbol_Table.addChild("else")
        self.visitBody(ctx.body())
        self.symbol_Table.goToParent()

    def visitWhileStatement(self, ctx:grammarCParser.WhileStatementContext):
        self.symbol_Table.addChild("while")
        self.visitCondition(ctx.condition())
        self.visitBody(ctx.body())
        self.symbol_Table.goToParent()

    def visitLoop(self, ctx:grammarCParser.WhileStatementContext):
        self.symbol_Table.addChild("if")
        self.visitForCondition(ctx.forCondition())
        self.visitBody(ctx.body())
        self.symbol_Table.goToParent()

    def visitRValue(self, ctx:grammarCParser.RValueContext):
        if(ctx.ID()!=None):
            if(self.symbol_Table.search(ctx.ID())==False):
                print("Error: Undeclared variable " + ctx.ID().getText())
                sys.exit()

        if(ctx.DIGIT()!=None):
            if(self.symbol_Table.prev_type != 'int'):
                print("Error: mismatched type, expected int")
                sys.exit()

        if(ctx.STR()!=None):
            if (self.symbol_Table.prev_type != 'char'):
                print("Error: mismatched type, expected char")
                sys.exit()

        if(ctx.FLT()!=None):
            if (self.symbol_Table.prev_type != 'float'):
                print("Error: mismatched type, expected float")
                sys.exit()

        if(ctx.BOOL()!=None):
            if (self.symbol_Table.prev_type != 'bool'):
                print("Error: mismatched type, expected bool")
                sys.exit()


    def visitLValue(self, ctx:grammarCParser.LValueContext):
        return ctx.getText()
        
