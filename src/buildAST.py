from grammar.grammarCVisitor import grammarCVisitor
from grammar.grammarCParser import grammarCParser
from AST import AST

class buildAST(grammarCVisitor):

    def __init__(self):
        self.ast = AST()

    def start(self, tree):
        self.visitProgram(tree)

    def visitProgram(self, ctx: grammarCParser.ProgramContext):
        self.ast.newChild("Program")
        self.visitChildren(ctx)
        self.ast.toDot()

    def visitFuncDef(self, ctx: grammarCParser.FuncDefContext):
        self.ast.toRoot()
        self.ast.newChild(ctx.getChild(1).getText() + "()")
        name = ctx.lValue().getText()
        self.visitArgList(ctx.argList())
        self.visitBody(ctx.body())

    def visitMainFunc(self, ctx: grammarCParser.MainFuncContext):
        self.ast.toRoot()
        self.ast.newChild("Main")
        self.visitChildren(ctx)

    def visitBody(self, ctx: grammarCParser.BodyContext):
        self.visitChildren(ctx)

    def visitStatement(self, ctx: grammarCParser.StatementContext):
        self.visitChildren(ctx)

    def visitDeclaration(self, ctx: grammarCParser.DeclarationContext):
        if(ctx.arrayDecl()==None):
            name = ctx.lValue().getText()
            self.ast.newChild(self.visitConstant(ctx.constant()) + " " + ctx.types().getText() + " " + self.visitPointer(
                ctx.pointer()) + " Dcl")
            self.ast.newChild(name)
            self.ast.toParent()
            self.ast.toParent()
        else:
            self.visitArrayDecl(ctx.arrayDecl())

    def visitDefinition(self, ctx: grammarCParser.DefinitionContext):
        self.ast.newChild(self.visitConstant(ctx.constant()) + " " + ctx.types().getText() + " " + self.visitPointer(
            ctx.pointer()) + " Def")
        self.visitChildren(ctx)
        self.ast.toParent()

    def visitAssignment(self, ctx: grammarCParser.AssignmentContext):
        self.ast.newChild("Assignment")
        temp = self.ast.currentNode.getParent()
        self.visitChildren(ctx)
        self.ast.currentNode=temp
    def visitArrayAssignment(self, ctx:grammarCParser.ArrayAssignmentContext):
        name = ctx.lValue().getText()
        name+='['
        if(ctx.DIGIT()!=None):
            name+=ctx.DIGIT().getText()
        elif(ctx.ID()!=None):
            name+=ctx.ID().getText()
        name+=']'
        self.ast.newChild(name)
        self.ast.toParent()
        self.visitArrayOptions(ctx.arrayOptions())
        self.ast.toParent()

    def visitFunctionCall(self, ctx: grammarCParser.FunctionCallContext):
        self.ast.newChild(ctx.getChild(0).getText() + "()")
        self.ast.toParent()

    def visitReturnStatement(self, ctx: grammarCParser.ReturnStatementContext):
        self.ast.newChild("Return")
        self.visitChildren(ctx)
        self.ast.toParent()

    def visitLValue(self, ctx: grammarCParser.LValueContext):
        self.ast.newChild(ctx.getText())
        self.ast.toParent()

    def visitRValue(self, ctx: grammarCParser.RValueContext):
        self.ast.newChild(ctx.getText())
        self.ast.toParent()

    def visitArrayOptions(self, ctx: grammarCParser.ArrayOptionsContext):
        self.ast.newChild(ctx.getText())
        self.ast.toParent()

    def visitOperation(self, ctx: grammarCParser.OperationContext):
        if (ctx.operator() != None):
            op = ctx.operator().getText()
            self.ast.newChild("Operation\n" + op)
        self.visitChildren(ctx)
        self.ast.toParent()

    def visitNextOperation(self, ctx: grammarCParser.NextOperationContext):
        if (ctx.operator() != None):
            op = ctx.operator().getText()
            self.ast.newChild("Operation\n" + op)
        self.visitChildren(ctx)
        if (ctx.getChild(0).getText() == '('):
            self.ast.toParent()

    def visitBaseOperation(self, ctx: grammarCParser.BaseOperationContext):
        if (ctx.operator() != None):
            op = ctx.operator().getText()
            self.ast.newChild("Operation\n" + op)
        self.visitChildren(ctx)
        if (ctx.getChild(0).getText() == '('):
            self.ast.toParent()

    def visitComparison(self, ctx: grammarCParser.ComparisonContext):
        self.visitChildren(ctx)
        self.ast.toParent()

    def visitIfStatement(self, ctx: grammarCParser.IfStatementContext):
        self.ast.newChild("if")
        self.ast.newChild(ctx.condition().getText())
        self.visitBody(ctx.body())
        self.ast.toParent()
        self.ast.toParent()

    def visitElifStatement(self, ctx: grammarCParser.ElifStatementContext):
        if_p = self.ast.getChild('if')
        if (if_p != False):
            self.ast.currentNode = if_p
        self.ast.newChild("else if\n" + ctx.condition().getText())
        self.visitBody(ctx.body())
        self.ast.toParent()

    def visitElseStatement(self, ctx: grammarCParser.ElseStatementContext):
        self.ast.newChild("else")
        self.visitBody(ctx.body())
        self.ast.toParent()
        self.ast.toParent()

    def visitWhileStatement(self, ctx: grammarCParser.WhileStatementContext):
        self.ast.newChild("while\n" + ctx.condition().getText())
        self.visitBody(ctx.body())
        self.ast.toParent()

    def visitLoop(self, ctx: grammarCParser.LoopContext):
        self.ast.newChild("for\n" + ctx.forCondition().getText())
        self.visitBody(ctx.body())
        self.ast.toParent()

    def visitPointer(self, ctx: grammarCParser.PointerContext):
        if (ctx == None or ctx == []):
            return ""
        else:
            return "Pointer"

    def visitConstant(self, ctx: grammarCParser.ConstantContext):
        if (ctx == None or ctx == []):
            return ""
        else:
            return "Constant"

    def visitReference(self, ctx: grammarCParser.ReferenceContext):
        if (ctx == None or ctx == []):
            return ""
        else:
            return "Reference"

    def visitArgList(self, ctx: grammarCParser.ArgListContext):
        if (ctx.getChildCount() != 0):
            typeList = ctx.types()
            idList = ctx.lValue()
