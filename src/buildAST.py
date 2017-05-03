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
        self.file.goRoot()
        self.file.newChild(ctx.getChild(1).getText() + "()")
        self.visitBody(ctx.body())


    def visitMainFunc(self, ctx:grammarCParser.MainFuncContext):
        self.file.goRoot()
        self.file.newChild("Main")
        self.visitChildren(ctx)

    def visitBody(self, ctx:grammarCParser.BodyContext):
        self.visitChildren(ctx)

    def visitStatement(self, ctx:grammarCParser.StatementContext):
        self.visitChildren(ctx)


    def visitDeclaration(self, ctx:grammarCParser.DeclarationContext):
        self.file.newChild("Declaration")
        self.file.newChild(ctx.types().getText())
        self.file.goBack()
        self.file.newChild(ctx.lValue().getText())
        self.file.goBack()
        self.file.goBack()

    def visitDefinition(self, ctx:grammarCParser.DefinitionContext):
        self.file.newChild("Definition")
        self.file.newChild(ctx.types().getText())
        self.file.goBack()
        self.visitChildren(ctx)
        self.file.goBack()

    def visitAssignment(self, ctx:grammarCParser.AssignmentContext):
        self.file.newChild("Assignment")
        self.visitChildren(ctx)
        self.file.goBack()

    def visitFunctionCall(self, ctx: grammarCParser.FunctionCallContext):
        self.file.newChild(ctx.getChild(0).getText() + "()")
        self.file.goBack()

    def visitConditional(self, ctx: grammarCParser.ConditionalContext):
        self.file.newChild(ctx.getChild(0).getText() + "\n" + ctx.getChild(2).getText())
        if(ctx.getChildCount()>7):
            self.visitBody(ctx.body()[0])
            self.file.newChild(ctx.getChild(7).getText())
            self.visitBody(ctx.body()[1])
            self.file.goBack()
            self.file.goBack()
            self.file.goBack()
        else:
            self.visitBody(ctx.body()[0])
            self.file.goBack()
        self.file.goBack()

    def visitReturnStatement(self, ctx: grammarCParser.ReturnStatementContext):
        self.file.newChild("Return")
        self.visitChildren(ctx)
        self.file.goBack()

    def visitKw(self, ctx: grammarCParser.KwContext):
        self.file.newChild(ctx.getChild(0).getText())
        self.visitChildren(ctx)
        self.file.goBack()

    def visitLValue(self, ctx:grammarCParser.LValueContext):
        self.file.newChild(ctx.getText())
        self.file.goBack()

    def visitRValue(self, ctx:grammarCParser.RValueContext):
        self.file.newChild(ctx.getText())
        self.file.goBack()

    def visitArrayOptions(self, ctx:grammarCParser.ArrayOptionsContext):
        self.file.newChild(ctx.getText())
        self.file.goBack()


    def visitOperation(self, ctx: grammarCParser.OperationContext):
        if(ctx.getChildCount()==3):
            op = self.visitOperator(ctx.operator())

        else:
            op = self.visitDeincrement(ctx.deincrement())

        self.file.newChild("Operation\n" + op)
        self.visitChildren(ctx)
        self.file.goBack()

    def visitDeincrement(self, ctx:grammarCParser.DeincrementContext):
        return ctx.getText()

    
    def visitOperator(self, ctx:grammarCParser.OperatorContext):
        return ctx.getText()


    def visitComparison(self, ctx: grammarCParser.ComparisonContext):
        self.visitChildren(ctx)
        self.file.goBack()

    
    """
    def visitNormalAssignment(self, ctx:grammarCParser.NormalAssignmentContext):
        self.file.newChild(str(ctx.lValue()[0]))
        self.file.noChild()
        if(len(ctx.rValue())==2):
            self.file.newChild(str(ctx.rValue()[1]))
            self.file.noChild()
            self.file.noChild()
        else:
            self.visitChildren(ctx)
            self.file.noChild()

    def visitArrayAssignment(self, ctx:grammarCParser.ArrayAssignmentContext):
        self.file.newChild(str(ctx.lValue()[0]))
        self.file.noChild()
        self.file.newChild(ctx.arrayOptions().getText())
        #self.visitChildren(ctx)
        self.file.noChild()


    def visitLit(self, ctx:grammarCParser.LitContext):
        self.file.newChild(ctx.getChild(0).getText())
        self.file.noChild()

    """
