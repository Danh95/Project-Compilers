from grammar.grammarCVisitor import grammarCVisitor
from grammar.grammarCParser import grammarCParser
from symbolTable import symbolTable
import sys

class buildSymbolTable(grammarCVisitor):

    def __init__(self, parser, filename):
        self.parser = parser
        self.symbol_Table = symbolTable()
        self.SP = 0
        end = filename.find('.c')
        filename = filename[:end]
        filename = filename[::-1]
        end = filename.find('/')
        if (end != -1):
            filename = filename[:end]
        filename = filename[::-1]
        self.file = open(filename + '.p', 'w')

        self.T = {'pointer':'a', 'bool':'b', 'char':'c', 'int':'i', 'float':'r'}

        self.op_prior = False
        self.op_prev = None

    def visitProgram(self, ctx:grammarCParser.ProgramContext):
        self.symbol_Table.addChild("Program")
        self.visitChildren(ctx)
        self.symbol_Table.goToParent()

    def visitMainFunc(self, ctx:grammarCParser.MainFuncContext):
        self.symbol_Table.add("Main", "mainfunction", ctx.getChild(0).getText())
        self.symbol_Table.addChild("Main")
        if(ctx.getChildCount()!=0):
            self.file.write("start:\n")
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
        t = ctx.types().getText()
        self.file.write("ldc " + str(self.T[t]) + " " + "0\n")
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

        t = self.symbol_Table.search(ctx.lValue().getText())
        self.file.write("ldo " + str(self.T[t[0]]) + " " + str(t[2]) + "\n")
        self.visitChildren(ctx)
        self.file.write("sro " + str(self.T[t[0]]) + " " + str(t[2]) + "\n")

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
        v = ctx.getText()
        if(ctx.ID()!=None):
            t = self.symbol_Table.search(ctx.ID())
            if(t==False):
                print("Error: Undeclared variable " + ctx.ID().getText())
                sys.exit()
            else:
                self.file.write("ldo " + str(self.T[t[0]]) + " " + str(t[2]) + "\n")

        if(ctx.DIGIT()!=None):
            if(self.symbol_Table.prev_type != 'int'):
                print("Error: mismatched type, expected int")
                sys.exit()
            else:
                self.file.write("ldc i " + v + "\n")

        if(ctx.STR()!=None):
            if (self.symbol_Table.prev_type != 'char'):
                print("Error: mismatched type, expected char")
                sys.exit()
            else:
                self.file.write("ldc c " + v + "\n")
        if(ctx.FLT()!=None):
            if (self.symbol_Table.prev_type != 'float'):
                print("Error: mismatched type, expected float")
                sys.exit()
            else:
                self.file.write("ldc r " + v + "\n")
        if(ctx.BOOL()!=None):
            if (self.symbol_Table.prev_type != 'bool'):
                print("Error: mismatched type, expected bool")
                sys.exit()
            else:
                self.file.write("ldc b " + v + "\n")

    def visitLValue(self, ctx:grammarCParser.LValueContext):
        return ctx.getText()
        
    def visitOperation(self, ctx:grammarCParser.OperationContext):
        if(ctx.getChild(1)!=ctx.operator()):
            s_prior = self.op_prior
            s_prev = self.op_prev
            self.op_prior = False

            self.visitOperation((ctx.operation())[0])
            self.op_prior = s_prior
            self.op_prev = s_prev

        if(len(ctx.rValue())!=0):
            if(ctx.rValue()[0].ID()!=None):
                t = self.symbol_Table.search(ctx.rValue()[0].getText())
            elif(ctx.rValue()[0].FLT()!=None):
                t = ["float"]
            elif(ctx.rValue()[0].DIGIT()!=None):
                t = ["int"]
            else:
                sys.exit()

            N = self.T[t[0]]

            op = ctx.operator().getText()
            if(op=="*"):
                self.visitRValue(ctx.rValue()[0])
                if(self.op_prior == True):
                    self.file.write(self.op_prev + str(N) + "\n")
                self.op_prev = "mull "
                self.op_prior = True
                self.visit(ctx.getChild(2))
                if((ctx.getChild(ctx.getChildCount()-1) in ctx.rValue()) and self.op_prior == True):
                    self.file.write(self.op_prev + str(N) + "\n")
            elif(op=="/"):
                self.visitRValue(ctx.rValue()[0])
                if (self.op_prior == True):
                    self.file.write(self.op_prev + str(N) + "\n")
                self.op_prev = "div "
                self.op_prior = True
                self.visit(ctx.getChild(2))
                if((ctx.getChild(ctx.getChildCount()-1) in ctx.rValue()) and self.op_prior == True):
                    self.file.write(self.op_prev + str(N) + "\n")

            elif(op=="+"):
                self.visitRValue(ctx.rValue()[0])
                if (self.op_prior == True):
                    self.file.write(self.op_prev + str(N) + "\n")
                self.op_prior = False
                self.visit(ctx.getChild(2))
                self.file.write("add " + str(N) + "\n")
            elif(op=="-"):
                self.visitRValue(ctx.rValue()[0])
                if (self.op_prior == True):
                    self.file.write(self.op_prev + str(N) + "\n")
                self.op_prior = False
                self.visit(ctx.getChild(2))
                self.file.write("sub " + str(N) + "\n")



        else:
            s_prior = self.op_prior
            s_prev = self.op_prev
            self.op_prior = False

            self.visitOperation((ctx.operation())[1])
            self.op_prior = s_prior
            self.op_prev = s_prev

    def visitDeincrement(self, ctx:grammarCParser.DeincrementContext):
        if(ctx.getText()=='++'):
            pass
        else:
            pass