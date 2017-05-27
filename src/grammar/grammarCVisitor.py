# Generated from ./src/grammar/grammarC.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .grammarCParser import grammarCParser
else:
    from grammarCParser import grammarCParser

# This class defines a complete generic visitor for a parse tree produced by grammarCParser.

class grammarCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by grammarCParser#program.
    def visitProgram(self, ctx:grammarCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#libraryList.
    def visitLibraryList(self, ctx:grammarCParser.LibraryListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#library.
    def visitLibrary(self, ctx:grammarCParser.LibraryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#lib.
    def visitLib(self, ctx:grammarCParser.LibContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#libname.
    def visitLibname(self, ctx:grammarCParser.LibnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#funcDefList.
    def visitFuncDefList(self, ctx:grammarCParser.FuncDefListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#funcDecl.
    def visitFuncDecl(self, ctx:grammarCParser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#typeList.
    def visitTypeList(self, ctx:grammarCParser.TypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#funcDef.
    def visitFuncDef(self, ctx:grammarCParser.FuncDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#argList.
    def visitArgList(self, ctx:grammarCParser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#body.
    def visitBody(self, ctx:grammarCParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#statements.
    def visitStatements(self, ctx:grammarCParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#statement.
    def visitStatement(self, ctx:grammarCParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#returnStatement.
    def visitReturnStatement(self, ctx:grammarCParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#parList.
    def visitParList(self, ctx:grammarCParser.ParListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#declaration.
    def visitDeclaration(self, ctx:grammarCParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#definition.
    def visitDefinition(self, ctx:grammarCParser.DefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#functionCall.
    def visitFunctionCall(self, ctx:grammarCParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#assignment.
    def visitAssignment(self, ctx:grammarCParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#normalAssignment.
    def visitNormalAssignment(self, ctx:grammarCParser.NormalAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#arrayAssignment.
    def visitArrayAssignment(self, ctx:grammarCParser.ArrayAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#arrayOptions.
    def visitArrayOptions(self, ctx:grammarCParser.ArrayOptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#conditional.
    def visitConditional(self, ctx:grammarCParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#ifStatement.
    def visitIfStatement(self, ctx:grammarCParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#elifStatement.
    def visitElifStatement(self, ctx:grammarCParser.ElifStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#elseStatement.
    def visitElseStatement(self, ctx:grammarCParser.ElseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#whileStatement.
    def visitWhileStatement(self, ctx:grammarCParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#loop.
    def visitLoop(self, ctx:grammarCParser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#condition.
    def visitCondition(self, ctx:grammarCParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#forCondition.
    def visitForCondition(self, ctx:grammarCParser.ForConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#deel1.
    def visitDeel1(self, ctx:grammarCParser.Deel1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#deel2.
    def visitDeel2(self, ctx:grammarCParser.Deel2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#deel3.
    def visitDeel3(self, ctx:grammarCParser.Deel3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#operation.
    def visitOperation(self, ctx:grammarCParser.OperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#nextOperation.
    def visitNextOperation(self, ctx:grammarCParser.NextOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#baseOperation.
    def visitBaseOperation(self, ctx:grammarCParser.BaseOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#plusplus.
    def visitPlusplus(self, ctx:grammarCParser.PlusplusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#kw.
    def visitKw(self, ctx:grammarCParser.KwContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#mainFunc.
    def visitMainFunc(self, ctx:grammarCParser.MainFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#argListMain.
    def visitArgListMain(self, ctx:grammarCParser.ArgListMainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#types.
    def visitTypes(self, ctx:grammarCParser.TypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#operator.
    def visitOperator(self, ctx:grammarCParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#comparison.
    def visitComparison(self, ctx:grammarCParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#deincrement.
    def visitDeincrement(self, ctx:grammarCParser.DeincrementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#pointer.
    def visitPointer(self, ctx:grammarCParser.PointerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#reference.
    def visitReference(self, ctx:grammarCParser.ReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#constant.
    def visitConstant(self, ctx:grammarCParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#endStatement.
    def visitEndStatement(self, ctx:grammarCParser.EndStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#assign.
    def visitAssign(self, ctx:grammarCParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#rValue.
    def visitRValue(self, ctx:grammarCParser.RValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarCParser#lValue.
    def visitLValue(self, ctx:grammarCParser.LValueContext):
        return self.visitChildren(ctx)



del grammarCParser