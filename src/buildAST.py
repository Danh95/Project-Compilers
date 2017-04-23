from grammar.grammarCVisitor import grammarCVisitor
from grammar.grammarCParser import grammarCParser
from writeAST import writeAST

class buildAST(grammarCVisitor):

    def __init__(self, parser):
        self.parser = parser
        self.file = writeAST()


    def visitProgram(self, ctx:grammarCParser.ProgramContext):
        self.file.programNode()
        self.visitChildren(ctx)
        self.file.convertFile()

    def visitFuncDef(self, ctx:grammarCParser.FuncDefContext):
        self.file.newStatement()
        self.file.newChild("Function definition")
        self.file.newChild(ctx.getChild(1).getText() + "()")


    def visitMainFunc(self, ctx:grammarCParser.MainFuncContext):
        self.visitChildren(ctx)
        self.file.noChild()

    def visitStatement(self, ctx:grammarCParser.StatementContext):
        self.file.newStatement()
        self.visitChildren(ctx)
        self.file.noChild()

    def visitDeclaration(self, ctx:grammarCParser.DeclarationContext):
        self.file.newChild("Declaration")
        self.file.newChild(ctx.types().getText())
        self.file.noChild()
        self.file.newChild(str(ctx.ID()[0]))
        self.file.noChild()

    def visitDefinition(self, ctx: grammarCParser.DefinitionContext):
        self.file.newChild("Definition")
        self.file.newChild(ctx.types().getText())
        self.file.noChild()
        self.visitChildren(ctx)
        self.file.noChild()

    def visitAssignment(self, ctx:grammarCParser.AssignmentContext):
        self.file.newChild("Assignment")
        self.visitChildren(ctx)
        self.file.noChild()

    def visitFunctionCall(self, ctx: grammarCParser.FunctionCallContext):
        self.file.newChild("FunctionCall")
        self.file.newChild(ctx.getChild(0).getText() + "()")
        self.file.noChild()
        self.file.noChild()

    def visitConditional(self, ctx: grammarCParser.ConditionalContext):
        self.file.newChild(ctx.getChild(0).getText())
        self.file.newChild(ctx.getChild(2).getText())
        self.file.noChild()
        #self.visitChildren(ctx)
        self.file.noChild()

    def visitReturnStatement(self, ctx: grammarCParser.ReturnStatementContext):
        self.file.newChild("Return")
        self.visitChildren(ctx)
        self.file.noChild()

    def visitOperation(self, ctx: grammarCParser.OperationContext):
        self.file.newChild("Operation")
        self.file.newChild(ctx.getChild(0).getText())
        self.file.noChild()


        if(ctx.getChildCount()==3):
            self.visitOperator(ctx.operator())
            self.file.noChild()

        self.file.newChild(ctx.getChild(ctx.getChildCount()-1).getText())
        self.file.noChild()
        self.file.noChild()


    def visitOperator(self, ctx:grammarCParser.OperatorContext):
        self.file.newChild(str(ctx.getChild(0).getText()))
        #self.visitChildren(ctx)
        self.file.noChild()


    def visitComparison(self, ctx: grammarCParser.ComparisonContext):
        self.visitChildren(ctx)
        self.file.noChild()

    def visitKw(self, ctx: grammarCParser.KwContext):
        self.file.newChild("Keyword")
        self.file.newChild(ctx.getChild(0).getText())
        self.file.noChild()
        self.visitChildren(ctx)
        self.file.noChild()

    def visitNormalAssignment(self, ctx:grammarCParser.NormalAssignmentContext):
        self.file.newChild(str(ctx.ID()[0]))
        self.file.noChild()
        if(len(ctx.ID())==2):
            self.file.newChild(str(ctx.ID()[1]))
            self.file.noChild()
            self.file.noChild()
        else:
            self.visitChildren(ctx)
            self.file.noChild()

    def visitArrayAssignment(self, ctx:grammarCParser.ArrayAssignmentContext):
        self.file.newChild(str(ctx.ID()[0]))
        self.file.noChild()
        self.file.newChild(ctx.arrayOptions().getText())
        #self.visitChildren(ctx)
        self.file.noChild()


    def visitLit(self, ctx:grammarCParser.LitContext):
        self.file.newChild(ctx.getChild(0).getText())
        self.file.noChild()


