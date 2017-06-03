# Generated from ./src/grammar/grammarC.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .grammarCParser import grammarCParser
else:
    from grammarCParser import grammarCParser

# This class defines a complete listener for a parse tree produced by grammarCParser.
class grammarCListener(ParseTreeListener):

    # Enter a parse tree produced by grammarCParser#program.
    def enterProgram(self, ctx:grammarCParser.ProgramContext):
        pass

    # Exit a parse tree produced by grammarCParser#program.
    def exitProgram(self, ctx:grammarCParser.ProgramContext):
        pass


    # Enter a parse tree produced by grammarCParser#libraryList.
    def enterLibraryList(self, ctx:grammarCParser.LibraryListContext):
        pass

    # Exit a parse tree produced by grammarCParser#libraryList.
    def exitLibraryList(self, ctx:grammarCParser.LibraryListContext):
        pass


    # Enter a parse tree produced by grammarCParser#library.
    def enterLibrary(self, ctx:grammarCParser.LibraryContext):
        pass

    # Exit a parse tree produced by grammarCParser#library.
    def exitLibrary(self, ctx:grammarCParser.LibraryContext):
        pass


    # Enter a parse tree produced by grammarCParser#lib.
    def enterLib(self, ctx:grammarCParser.LibContext):
        pass

    # Exit a parse tree produced by grammarCParser#lib.
    def exitLib(self, ctx:grammarCParser.LibContext):
        pass


    # Enter a parse tree produced by grammarCParser#libname.
    def enterLibname(self, ctx:grammarCParser.LibnameContext):
        pass

    # Exit a parse tree produced by grammarCParser#libname.
    def exitLibname(self, ctx:grammarCParser.LibnameContext):
        pass


    # Enter a parse tree produced by grammarCParser#funcDefList.
    def enterFuncDefList(self, ctx:grammarCParser.FuncDefListContext):
        pass

    # Exit a parse tree produced by grammarCParser#funcDefList.
    def exitFuncDefList(self, ctx:grammarCParser.FuncDefListContext):
        pass


    # Enter a parse tree produced by grammarCParser#funcDecl.
    def enterFuncDecl(self, ctx:grammarCParser.FuncDeclContext):
        pass

    # Exit a parse tree produced by grammarCParser#funcDecl.
    def exitFuncDecl(self, ctx:grammarCParser.FuncDeclContext):
        pass


    # Enter a parse tree produced by grammarCParser#typeList.
    def enterTypeList(self, ctx:grammarCParser.TypeListContext):
        pass

    # Exit a parse tree produced by grammarCParser#typeList.
    def exitTypeList(self, ctx:grammarCParser.TypeListContext):
        pass


    # Enter a parse tree produced by grammarCParser#funcDef.
    def enterFuncDef(self, ctx:grammarCParser.FuncDefContext):
        pass

    # Exit a parse tree produced by grammarCParser#funcDef.
    def exitFuncDef(self, ctx:grammarCParser.FuncDefContext):
        pass


    # Enter a parse tree produced by grammarCParser#argList.
    def enterArgList(self, ctx:grammarCParser.ArgListContext):
        pass

    # Exit a parse tree produced by grammarCParser#argList.
    def exitArgList(self, ctx:grammarCParser.ArgListContext):
        pass


    # Enter a parse tree produced by grammarCParser#body.
    def enterBody(self, ctx:grammarCParser.BodyContext):
        pass

    # Exit a parse tree produced by grammarCParser#body.
    def exitBody(self, ctx:grammarCParser.BodyContext):
        pass


    # Enter a parse tree produced by grammarCParser#statement.
    def enterStatement(self, ctx:grammarCParser.StatementContext):
        pass

    # Exit a parse tree produced by grammarCParser#statement.
    def exitStatement(self, ctx:grammarCParser.StatementContext):
        pass


    # Enter a parse tree produced by grammarCParser#returnStatement.
    def enterReturnStatement(self, ctx:grammarCParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by grammarCParser#returnStatement.
    def exitReturnStatement(self, ctx:grammarCParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by grammarCParser#parList.
    def enterParList(self, ctx:grammarCParser.ParListContext):
        pass

    # Exit a parse tree produced by grammarCParser#parList.
    def exitParList(self, ctx:grammarCParser.ParListContext):
        pass


    # Enter a parse tree produced by grammarCParser#declaration.
    def enterDeclaration(self, ctx:grammarCParser.DeclarationContext):
        pass

    # Exit a parse tree produced by grammarCParser#declaration.
    def exitDeclaration(self, ctx:grammarCParser.DeclarationContext):
        pass


    # Enter a parse tree produced by grammarCParser#arrayDecl.
    def enterArrayDecl(self, ctx:grammarCParser.ArrayDeclContext):
        pass

    # Exit a parse tree produced by grammarCParser#arrayDecl.
    def exitArrayDecl(self, ctx:grammarCParser.ArrayDeclContext):
        pass


    # Enter a parse tree produced by grammarCParser#definition.
    def enterDefinition(self, ctx:grammarCParser.DefinitionContext):
        pass

    # Exit a parse tree produced by grammarCParser#definition.
    def exitDefinition(self, ctx:grammarCParser.DefinitionContext):
        pass


    # Enter a parse tree produced by grammarCParser#functionCall.
    def enterFunctionCall(self, ctx:grammarCParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by grammarCParser#functionCall.
    def exitFunctionCall(self, ctx:grammarCParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by grammarCParser#assignment.
    def enterAssignment(self, ctx:grammarCParser.AssignmentContext):
        pass

    # Exit a parse tree produced by grammarCParser#assignment.
    def exitAssignment(self, ctx:grammarCParser.AssignmentContext):
        pass


    # Enter a parse tree produced by grammarCParser#normalAssignment.
    def enterNormalAssignment(self, ctx:grammarCParser.NormalAssignmentContext):
        pass

    # Exit a parse tree produced by grammarCParser#normalAssignment.
    def exitNormalAssignment(self, ctx:grammarCParser.NormalAssignmentContext):
        pass


    # Enter a parse tree produced by grammarCParser#arrayAssignment.
    def enterArrayAssignment(self, ctx:grammarCParser.ArrayAssignmentContext):
        pass

    # Exit a parse tree produced by grammarCParser#arrayAssignment.
    def exitArrayAssignment(self, ctx:grammarCParser.ArrayAssignmentContext):
        pass


    # Enter a parse tree produced by grammarCParser#arrayOptions.
    def enterArrayOptions(self, ctx:grammarCParser.ArrayOptionsContext):
        pass

    # Exit a parse tree produced by grammarCParser#arrayOptions.
    def exitArrayOptions(self, ctx:grammarCParser.ArrayOptionsContext):
        pass


    # Enter a parse tree produced by grammarCParser#conditional.
    def enterConditional(self, ctx:grammarCParser.ConditionalContext):
        pass

    # Exit a parse tree produced by grammarCParser#conditional.
    def exitConditional(self, ctx:grammarCParser.ConditionalContext):
        pass


    # Enter a parse tree produced by grammarCParser#ifStatement.
    def enterIfStatement(self, ctx:grammarCParser.IfStatementContext):
        pass

    # Exit a parse tree produced by grammarCParser#ifStatement.
    def exitIfStatement(self, ctx:grammarCParser.IfStatementContext):
        pass


    # Enter a parse tree produced by grammarCParser#elifStatement.
    def enterElifStatement(self, ctx:grammarCParser.ElifStatementContext):
        pass

    # Exit a parse tree produced by grammarCParser#elifStatement.
    def exitElifStatement(self, ctx:grammarCParser.ElifStatementContext):
        pass


    # Enter a parse tree produced by grammarCParser#elseStatement.
    def enterElseStatement(self, ctx:grammarCParser.ElseStatementContext):
        pass

    # Exit a parse tree produced by grammarCParser#elseStatement.
    def exitElseStatement(self, ctx:grammarCParser.ElseStatementContext):
        pass


    # Enter a parse tree produced by grammarCParser#whileStatement.
    def enterWhileStatement(self, ctx:grammarCParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by grammarCParser#whileStatement.
    def exitWhileStatement(self, ctx:grammarCParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by grammarCParser#loop.
    def enterLoop(self, ctx:grammarCParser.LoopContext):
        pass

    # Exit a parse tree produced by grammarCParser#loop.
    def exitLoop(self, ctx:grammarCParser.LoopContext):
        pass


    # Enter a parse tree produced by grammarCParser#condition.
    def enterCondition(self, ctx:grammarCParser.ConditionContext):
        pass

    # Exit a parse tree produced by grammarCParser#condition.
    def exitCondition(self, ctx:grammarCParser.ConditionContext):
        pass


    # Enter a parse tree produced by grammarCParser#forCondition.
    def enterForCondition(self, ctx:grammarCParser.ForConditionContext):
        pass

    # Exit a parse tree produced by grammarCParser#forCondition.
    def exitForCondition(self, ctx:grammarCParser.ForConditionContext):
        pass


    # Enter a parse tree produced by grammarCParser#deel1.
    def enterDeel1(self, ctx:grammarCParser.Deel1Context):
        pass

    # Exit a parse tree produced by grammarCParser#deel1.
    def exitDeel1(self, ctx:grammarCParser.Deel1Context):
        pass


    # Enter a parse tree produced by grammarCParser#deel2.
    def enterDeel2(self, ctx:grammarCParser.Deel2Context):
        pass

    # Exit a parse tree produced by grammarCParser#deel2.
    def exitDeel2(self, ctx:grammarCParser.Deel2Context):
        pass


    # Enter a parse tree produced by grammarCParser#deel3.
    def enterDeel3(self, ctx:grammarCParser.Deel3Context):
        pass

    # Exit a parse tree produced by grammarCParser#deel3.
    def exitDeel3(self, ctx:grammarCParser.Deel3Context):
        pass


    # Enter a parse tree produced by grammarCParser#operation.
    def enterOperation(self, ctx:grammarCParser.OperationContext):
        pass

    # Exit a parse tree produced by grammarCParser#operation.
    def exitOperation(self, ctx:grammarCParser.OperationContext):
        pass


    # Enter a parse tree produced by grammarCParser#nextOperation.
    def enterNextOperation(self, ctx:grammarCParser.NextOperationContext):
        pass

    # Exit a parse tree produced by grammarCParser#nextOperation.
    def exitNextOperation(self, ctx:grammarCParser.NextOperationContext):
        pass


    # Enter a parse tree produced by grammarCParser#baseOperation.
    def enterBaseOperation(self, ctx:grammarCParser.BaseOperationContext):
        pass

    # Exit a parse tree produced by grammarCParser#baseOperation.
    def exitBaseOperation(self, ctx:grammarCParser.BaseOperationContext):
        pass


    # Enter a parse tree produced by grammarCParser#plusplus.
    def enterPlusplus(self, ctx:grammarCParser.PlusplusContext):
        pass

    # Exit a parse tree produced by grammarCParser#plusplus.
    def exitPlusplus(self, ctx:grammarCParser.PlusplusContext):
        pass


    # Enter a parse tree produced by grammarCParser#kw.
    def enterKw(self, ctx:grammarCParser.KwContext):
        pass

    # Exit a parse tree produced by grammarCParser#kw.
    def exitKw(self, ctx:grammarCParser.KwContext):
        pass


    # Enter a parse tree produced by grammarCParser#mainFunc.
    def enterMainFunc(self, ctx:grammarCParser.MainFuncContext):
        pass

    # Exit a parse tree produced by grammarCParser#mainFunc.
    def exitMainFunc(self, ctx:grammarCParser.MainFuncContext):
        pass


    # Enter a parse tree produced by grammarCParser#argListMain.
    def enterArgListMain(self, ctx:grammarCParser.ArgListMainContext):
        pass

    # Exit a parse tree produced by grammarCParser#argListMain.
    def exitArgListMain(self, ctx:grammarCParser.ArgListMainContext):
        pass


    # Enter a parse tree produced by grammarCParser#types.
    def enterTypes(self, ctx:grammarCParser.TypesContext):
        pass

    # Exit a parse tree produced by grammarCParser#types.
    def exitTypes(self, ctx:grammarCParser.TypesContext):
        pass


    # Enter a parse tree produced by grammarCParser#operator.
    def enterOperator(self, ctx:grammarCParser.OperatorContext):
        pass

    # Exit a parse tree produced by grammarCParser#operator.
    def exitOperator(self, ctx:grammarCParser.OperatorContext):
        pass


    # Enter a parse tree produced by grammarCParser#comparison.
    def enterComparison(self, ctx:grammarCParser.ComparisonContext):
        pass

    # Exit a parse tree produced by grammarCParser#comparison.
    def exitComparison(self, ctx:grammarCParser.ComparisonContext):
        pass


    # Enter a parse tree produced by grammarCParser#deincrement.
    def enterDeincrement(self, ctx:grammarCParser.DeincrementContext):
        pass

    # Exit a parse tree produced by grammarCParser#deincrement.
    def exitDeincrement(self, ctx:grammarCParser.DeincrementContext):
        pass


    # Enter a parse tree produced by grammarCParser#pointer.
    def enterPointer(self, ctx:grammarCParser.PointerContext):
        pass

    # Exit a parse tree produced by grammarCParser#pointer.
    def exitPointer(self, ctx:grammarCParser.PointerContext):
        pass


    # Enter a parse tree produced by grammarCParser#reference.
    def enterReference(self, ctx:grammarCParser.ReferenceContext):
        pass

    # Exit a parse tree produced by grammarCParser#reference.
    def exitReference(self, ctx:grammarCParser.ReferenceContext):
        pass


    # Enter a parse tree produced by grammarCParser#constant.
    def enterConstant(self, ctx:grammarCParser.ConstantContext):
        pass

    # Exit a parse tree produced by grammarCParser#constant.
    def exitConstant(self, ctx:grammarCParser.ConstantContext):
        pass


    # Enter a parse tree produced by grammarCParser#endStatement.
    def enterEndStatement(self, ctx:grammarCParser.EndStatementContext):
        pass

    # Exit a parse tree produced by grammarCParser#endStatement.
    def exitEndStatement(self, ctx:grammarCParser.EndStatementContext):
        pass


    # Enter a parse tree produced by grammarCParser#assign.
    def enterAssign(self, ctx:grammarCParser.AssignContext):
        pass

    # Exit a parse tree produced by grammarCParser#assign.
    def exitAssign(self, ctx:grammarCParser.AssignContext):
        pass


    # Enter a parse tree produced by grammarCParser#rValue.
    def enterRValue(self, ctx:grammarCParser.RValueContext):
        pass

    # Exit a parse tree produced by grammarCParser#rValue.
    def exitRValue(self, ctx:grammarCParser.RValueContext):
        pass


    # Enter a parse tree produced by grammarCParser#lValue.
    def enterLValue(self, ctx:grammarCParser.LValueContext):
        pass

    # Exit a parse tree produced by grammarCParser#lValue.
    def exitLValue(self, ctx:grammarCParser.LValueContext):
        pass


