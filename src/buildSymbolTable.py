from grammar.grammarCVisitor import grammarCVisitor
from grammar.grammarCParser import grammarCParser
from symbolTable import symbolTable
import sys

class buildSymbolTable(grammarCVisitor):

    def __init__(self, parser, filename):
        self.parser = parser
        self.symbol_Table = symbolTable()
        self.SP = 2
        end = filename.find('.c')
        filename = filename[:end]
        filename = filename[::-1]
        end = filename.find('/')
        if (end != -1):
            filename = filename[:end]
        filename = filename[::-1]
        self.file = open(filename + '.p', 'w')

        self.T = {'pointer':'a', 'bool':'b', 'char':'c', 'int':'i', 'float':'r'}

        self.op_state = False
        self.op_prev = None
        self.N = None

        self.IF = 0
        self.WH = 0

        self.lc = 0
        self.ec = 0

        self.inDef = False

    def visitProgram(self, ctx:grammarCParser.ProgramContext):
        self.symbol_Table.addChild("Program")
        self.file.write("ujp start\n")
        self.visitChildren(ctx)
        self.symbol_Table.goToParent()

    def visitLibname(self, ctx:grammarCParser.LibnameContext):
        if(ctx.getText()=='stdio'):
            self.symbol_Table.add("scanf", "function definition", 'int')
            self.file.write("scanfd:\nin d\nsto i\n")
            self.file.write("scanfi:\nin i\nsto i\n")
            self.file.write("scanfc:\nin c\nsto c\n")
            #scanfs voor string met array
            self.symbol_Table.add("printf", "function definition", 'int')
            self.file.write("printfd:\nout i\n")
            self.file.write("printfi:\nout i\n")
            self.file.write("printfc:\nout c\n")


    def visitMainFunc(self, ctx:grammarCParser.MainFuncContext):
        self.symbol_Table.add("Main", "mainfunction", ctx.getChild(0).getText())
        self.symbol_Table.addChild("Main")
        if(ctx.getChildCount()!=0):
            self.file.write("start:\n")
        self.visitChildren(ctx)
        self.file.write("hlt\n")
        self.symbol_Table.goToParent()

    def visitFuncDef(self, ctx:grammarCParser.FuncDefContext):
        name = self.visitLValue(ctx.lValue())
        if(ctx.argList()!=None):
            arg = ctx.argList().types()
            for i in arg:
                name+=str(i.getText())
        self.symbol_Table.add(name, "function definition", self.visitTypes(ctx.types()))
        self.symbol_Table.addChild(name)
        self.SP += len(ctx.argList().types())
        self.file.write(ctx.lValue().getText() +":\n")
        stackP = self.SP
        self.file.write("ssp \n")
        self.visitChildren(ctx)
        #do something to return
        self.SP = stackP
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
        if(ctx.arrayDecl()==None):
            name = self.visitLValue(ctx.lValue())
            if(self.symbol_Table.search(ctx.lValue().getText())!=False):
                print("Error: Redeclaration of " + ctx.lValue().getText())
                sys.exit()
            t = ctx.types().getText()
            if(ctx.pointer()!=[]):
                for i in ctx.pointer():
                    t += '*'
                self.file.write("ldc " + str(self.T["pointer"]) + " " + "0\n")

            else:
                self.file.write("ldc " + str(self.T[t]) + " " + "0\n")
            self.symbol_Table.add(name, "var declaration", t, self.SP)

            self.SP += 1
        else:
            self.visitArrayDecl(ctx.arrayDecl())

    def visitArrayDecl(self, ctx:grammarCParser.ArrayDeclContext):
        name = self.visitLValue(ctx.lValue())
        if (self.symbol_Table.search(ctx.lValue().getText()) != False):
            print("Error: Redeclaration of " + ctx.lValue().getText())
            sys.exit()
        t = 'array'
        self.file.write("ldc a " + str(self.SP+1) + "\n")
        self.SP += 1
        if(ctx.DIGIT()!=None):
            for i in range(0, int(ctx.DIGIT().getText())):
                self.file.write("ldc i 0\n")
                self.SP += 1

        else:
            print("Error: array index not validatable")
            sys.exit()
        self.symbol_Table.add(name, ctx.types().getText(), t, self.SP)

        self.SP += 1
    def visitDefinition(self, ctx:grammarCParser.DefinitionContext):
        self.inDef = True
        if(ctx.assignment().normalAssignment()!=None):
            name = ctx.assignment().normalAssignment().lValue().getText()
            if(self.symbol_Table.search(name)!=False):
                print("Error: Redefinition of " + name)
                sys.exit()
            t = ctx.types().getText()
            if (ctx.pointer() != []):
                for i in ctx.pointer():
                    t += '*'
                self.file.write("ldc " + str(self.T["pointer"]) + " " + "0\n")
            else:
                self.file.write("ldc " + str(self.T[t]) + " " + "0\n")
            self.symbol_Table.add(name, "var declaration", t, self.SP)
            self.file.write("ldc a " + str(self.SP) +"\n")
            self.SP += 1
            self.visitAssignment(ctx.assignment())
        else:
            name = ctx.assignment().arrayAssignment().lValue().getText()
            s = self.symbol_Table.search(name)
            if(s!=False):
                print("Error: Redefinition of " + name)
                sys.exit()
            self.file.write("ldc " + str(self.T[ctx.types().getText()]) + " 0\n")
            self.SP += 1

            self.file.write("ldc a " + str(self.SP+1) + "\n")
            self.SP += 1

        self.inDef = False

    def visitFunctionCall(self, ctx:grammarCParser.FunctionCallContext):
        name = ctx.lValue().getText()
        arg = ctx.parList().rValue()
        stdio = {'s' : 'string', 'd' : 'int', 'i' : 'int', 'c' : 'char'}
        scanf_d = {'s' : 'scanfs','d' : 'scanfd','i' : 'scanfi','c' : 'scanfc'}
        printf_d = {'s' : 'printfs','d' : 'printfd','i' : 'printfi','c' : 'printfc'}
        string = arg[0].getText()
        string = string[1:-1]
        speci = []
        if(name=='scanf' or name=='printf'):
            #herdefinieren van scanf zonder parameters kan voor problemen zorgen
            i=0
            while(i<len(string)):
                if(string[i]=='%'):
                    if((stdio.get(string[i+1], (0, "error"))==(0,"error")) or (string[i+1]==" ")):
                        print("Error: incorrect specifier")
                        sys.exit()
                    else:
                        speci.append(string[i+1])
                        i+=1
                else:
                    if(name=='printf'):
                        if((string[i]=="\\" and string[i+1]=='n')):
                            self.file.write("ldc c \'\\n\'\n")
                            i += 1

                        elif(string[i]=='\\' and string[i+1]=='\\'):
                            self.file.write("ldc c \'\\\\'\n")
                            i += 1

                        else:

                            self.file.write("ldc c " + "\'" + str(string[i]) + "\'\n")
                        self.file.write("out c\n")
                i+=1
            if(len(speci)!=(len(arg)-1)):
                print("Error: incorrect number of specifiers")
                sys.exit()
            for i in arg[1:]:
                var = i.getText()
                t = speci.pop(0)
                var.replace("*", "")
                var.replace("&", "")
                entry = self.symbol_Table.search(var)
                if(entry==False):
                    print("Error: " + i.getText() + " does not exit")
                    sys.exit()
                else:
                    #type check
                    if(entry[0]!=stdio[t]):
                        print("Error: specifier does not match variable")
                        sys.exit()
                self.visitRValue(i)
                if(name=='scanf'):
                    self.file.write("ujp " + scanf_d[t] + "\n")
                else:
                    self.file.write("ujp " + printf_d[t] + "\n")



        else:
            for i in arg:
                if(i.ID()!=None):
                    s = self.symbol_Table.search(i.getText())
                    name += str(s[0])
                elif(i.DIGIT()!=None):
                    name += 'int'
                elif (i.BOOL() != None):
                    name += 'bool'
                elif (i.STR() != None):
                    name += 'char'
                elif (i.FLT() != None):
                    name += 'float'

            st = self.symbol_Table.search(name)
            if(st==False):
                print("Error: Function called before definition, unvalid reference to " + ctx.lValue().getText())
                sys.exit()
            self.file.write("mst " + str(st[3]) + "\n")
            self.visit(ctx.parList())
            self.file.write("cup " + str(len(arg)) + " "+ ctx.lValue().getText() + "\n")
                    #TODO len(arg)+space of array

    def visitNormalAssignment(self, ctx:grammarCParser.NormalAssignmentContext):
        self.symbol_Table.resetType()
        if(self.symbol_Table.search(ctx.lValue().getText())==False):
            print("Error: Assignment before declaration, unvalid reference to " + ctx.lValue().getText())
            sys.exit()

        t = self.symbol_Table.search(ctx.lValue().getText())
        self.visitChildren(ctx)
        if((t[0])[-1]=="*"):
            self.file.write("sto a \n")
        else:
            self.file.write("sto " + str(self.T[t[0]]) + "\n")

    def visitArrayAssignment(self, ctx:grammarCParser.ArrayAssignmentContext):
        self.symbol_Table.resetType()
        if(self.symbol_Table.search(ctx.lValue().getText())==False):
            print("Error: Assignment before declaration, invalid reference to " + ctx.lValue().getText())
            sys.exit()

        if(self.inDef):
            if(ctx.DIGIT()!=None):
                self.file.write("ldc  0\n")
                self.SP += 1
                self.file.write("ldo a " + str(self.SP))
                for i in range(1, int(ctx.DIGIT().getText())):
                    self.file.write("ldc i 0\n")
                    self.SP += 1
            else:
                print("Error: array index not validatable")
                sys.exit()
        self.visitChildren(ctx)

    def visitConditional(self, ctx:grammarCParser.ConditionalContext):
        self.visitChildren(ctx)
        self.file.write("endCond" + str(self.ec) + ":\n")
        self.ec+=1

    def visitIfStatement(self, ctx:grammarCParser.IfStatementContext):
        self.symbol_Table.addChild("if")
        self.visitCondition(ctx.condition())
        self.file.write("fjp l" + str(self.lc) + "\n")
        self.visitBody(ctx.body())
        self.file.write("ujp endCond" + str(self.ec) +"\n")
        self.symbol_Table.goToParent()

    def visitElifStatement(self, ctx:grammarCParser.ElifStatementContext):
        self.symbol_Table.addChild("else if")
        self.file.write("l" + str(self.lc) + ":\n")
        self.visitCondition(ctx.condition())
        self.lc+=1
        self.file.write("fjp l" + str(self.lc) + "\n")
        self.visitBody(ctx.body())
        self.file.write("ujp endCond" + str(self.ec) +"\n")
        self.symbol_Table.goToParent()

    def visitElseStatement(self, ctx:grammarCParser.ElseStatementContext):
        self.symbol_Table.addChild("else")
        self.file.write("l" + str(self.lc) + ":\n")
        self.lc += 1
        self.visitBody(ctx.body())
        self.file.write("ujp endCond" + str(self.ec) +"\n")
        self.symbol_Table.goToParent()

    def visitWhileStatement(self, ctx:grammarCParser.WhileStatementContext):
        self.symbol_Table.addChild("while")
        self.lc += 1
        self.file.write("ujp l" + str(self.lc) + "\nl" + str(self.lc) + ":\n")
        self.visitCondition(ctx.condition())
        self.file.write("fjp endCond" + str(self.ec) + "\n")
        self.visitBody(ctx.body())
        self.file.write("ujp l" + str(self.lc) + "\n")
        self.symbol_Table.goToParent()

    def visitLoop(self, ctx:grammarCParser.WhileStatementContext):
        self.symbol_Table.addChild("if")
        self.visitForCondition(ctx.forCondition())
        self.visitBody(ctx.body())
        self.symbol_Table.goToParent()

    def visitCondition(self, ctx:grammarCParser.ConditionContext):
        DC = {'<' : 'les', '>' : 'gtr', '==' : 'eq', '>=' : 'geq', '<=' : 'leq', '!=' : 'neq'}
        if(ctx.comparison()!=None):
            type1 = None;
            type2 = None;
            if((ctx.rValue())[0].ID()!=None):
                type1 = (self.symbol_Table.search((ctx.rValue())[0].getText()))
            if((ctx.rValue())[1].ID()!=None):
                type2 = (self.symbol_Table.search((ctx.rValue())[1].getText()))
            if(type1==False or type2==False):
                print("Error: argument not declared before comparison")
                sys.exit()
            if ((ctx.rValue())[0].ID() != None and (ctx.rValue())[1].ID() != None):
                if(str(type1[0])==str(type2[0])):
                    self.file.write("ldo " + str(self.T[type1[0]]) + " " + str(type1[2]) + "\n")
                    self.file.write("ldo " + str(self.T[type2[0]]) + " " + str(type2[2]) + "\n")
                    self.file.write(str(DC[ctx.comparison().getText()]) + " " + str(self.T[type1[0]]) + "\n")
                else:
                    print("Error: Type mismatched")
                    sys.exit()

            elif(type1!=None and type2==None):
                self.file.write("ldo " + str(self.T[type1[0]]) + " " + str(type1[2]) + "\n")
                if((ctx.rValue())[1].DIGIT()!=None):
                    type2='int'
                elif((ctx.rValue())[1].STR()!=None):
                    type2='char'
                elif((ctx.rValue())[1].FLT()!=None):
                    type2='float'
                elif((ctx.rValue())[1].BOOL()!=None):
                    type2='bool'

                if(str(type1[0])==type2):
                    if(type2=='char'):
                        self.file.write("ldc " + str(self.T[type2]) + " \'" + (ctx.rValue())[1].getText() + "\'\n")
                        self.SP += 1

                    else:
                        self.file.write("ldc " + str(self.T[type2]) + " " + (ctx.rValue())[1].getText() + "\n")
                        self.SP += 1

                    self.file.write(str(DC[ctx.comparison().getText()]) + " " + self.T[type2] + "\n")

                else:
                    sys.exit()

            elif(type1==None and type2!=None):
                self.file.write("ldo " + str(self.T[type2[0]]) + " " + str(type2[2]) + "\n")
                if ((ctx.rValue())[0].DIGIT() != None):
                    type1 = 'int'
                elif ((ctx.rValue())[0].STR() != None):
                    type1 = 'char'
                elif ((ctx.rValue())[0].FLT() != None):
                    type1 = 'float'
                elif ((ctx.rValue())[0].BOOL() != None):
                    type1 = 'bool'

                if (type1 == str(type2[0])):
                    if(type1=='char'):
                        self.file.write("ldc " + self.T[type1] + " \'" + (ctx.rValue())[0].getText() + "\'\n")
                    else:
                        self.file.write("ldc " + self.T[type1] + " "+ (ctx.rValue())[0].getText() + "\n")
                    self.file.write(str(DC[ctx.comparison().getText()]) + " " + self.T[type1] + "\n")

                else:
                    print("Error: Type mismatched")

                    sys.exit()

            elif(type1==None and type2==None):
                if((ctx.rValue())[0].DIGIT()!=None and (ctx.rValue())[1].DIGIT()!=None):
                    self.write("ldc i " + str((ctx.rValue()[0]).getText) + "\n")
                    self.write("ldc i " + str((ctx.rValue()[1]).getText) + "\n")
                    self.file.write(str(DC[ctx.comparison().getText()]) + " i\n")
                elif((ctx.rValue())[0].STR()!=None and (ctx.rValue())[1].STR()!=None):
                    self.write("ldc c " + str((ctx.rValue()[0]).getText) + "\n")
                    self.write("ldc c " + str((ctx.rValue()[1]).getText) + "\n")
                    self.file.write(str(DC[ctx.comparison().getText()]) + " c\n")
                elif((ctx.rValue())[0].FLT() != None and (ctx.rValue())[1].FLT()!= None):
                    self.write("ldc r " + str((ctx.rValue()[0]).getText) + "\n")
                    self.write("ldc r " + str((ctx.rValue()[1]).getText) + "\n")
                    self.file.write(str(DC[ctx.comparison().getText()]) + " r\n")
                elif((ctx.rValue())[0].BOOL()!=None and (ctx.rValue())[1].BOOL()!=None):
                    self.write("ldc b " + str((ctx.rValue()[0]).getText) + "\n")
                    self.write("ldc b " + str((ctx.rValue()[1]).getText) + "\n")
                    self.file.write(str(DC[ctx.comparison().getText()]) + " b\n")

                else:
                    print("Error: Type mismatched")

                    sys.exit()
                self.SP += 1

            elif(ctx.condition()!=None):
                self.visitCondition(ctx.condition())
                self.file.write("ldc b 1\nneq b\n")
                self.SP += 1

            elif(ctx.getChildCount()==2):
                if ((ctx.rValue())[0].DIGIT() != None or (ctx.rValue())[0].BOOL() != None):
                    if ((ctx.rValue())[0].getText() == "0"):
                        self.file.write("ldc b 1\n")
                    else:
                        self.file.write("ldc b 0\n")
                    self.SP += 1

                else:
                    print("ERROR: unsupported type for comparison")
                    sys.exit()
            elif(ctx.getChildCount()==1):
                if((ctx.rValue())[0].DIGIT()!=None or (ctx.rValue())[0].BOOL()!=None):
                    if((ctx.rValue())[0].getText()=="0"):
                        self.file.write("ldc b 0\n")
                    else:
                        self.file.write("ldc b 1\n")
                    self.SP += 1

                else:
                    print("ERROR: unsupported type for comparison")
                    sys.exit()



    def visitRValue(self, ctx:grammarCParser.RValueContext):
        v = ctx.getText()
        if(ctx.ID()!=[]):

            if (ctx.pointer() != []):
                for i in ctx.pointer():
                    self.symbol_Table.prev_type += "*"
            elif (ctx.reference() != []):
                for i in ctx.reference():
                    if (self.symbol_Table.prev_type[-1] == "*"):
                        self.symbol_Table.prev_type = self.symbol_Table.prev_type[:-1]
                    else:
                        print("Error: Unexpected pointer type")
                        sys.exit()


            else:
                self.file.write("ldc a " + str(t[2]) + "\n")
                self.SP += 1
                if (ctx.pointer() != []):
                    for i in ctx.pointer():
                        self.file.write("ind a\n")
                elif (ctx.reference() != []):
                    self.file.write("ldo a " + str(t[2]) + "\n")
                    for i in range(0, len(ctx.reference()) - 1):
                        self.SP += 1
                        self.file.write("ldo a " + str(self.SP - 1) + "\n")
                if (self.T.get(self.symbol_Table.prev_type, (0, "error")) != (0, "error")):
                    self.file.write("ind " + str(self.T[t[0]]) + "\n")
                else:
                    self.file.write("ind a\n")
            if(len(ctx.ID())==2):
                pr = self.symbol_Table.prev_type
                self.symbol_Table.prev_type = "array"
                t = self.symbol_Table.search(ctx.ID()[0])
                if (t == False):
                    print("Error: Undeclared variable " + ctx.ID().getText())
                    sys.exit()
                x = self.search(ctx.ID()[1].getText())
                if(x[0]!='int'):
                    print("Error: wrong index type")
                    sys.exit()
                else:
                    self.file.write("ldo a " + str(t[2]) + "\n")
                    self.file.write("ldo i " + str(x[2]) + "\n")
                    self.file.write("ixa 1\n")
                    self.file.write("ind i\n")
                self.symbol_Table.prev_type = pr

                if (pr == t[0]):
                    print("Error: ")
                    sys.exit()
            elif(ctx.DIGIT()!=None):
                pr = self.symbol_Table.prev_type
                self.symbol_Table.prev_type="array"
                t = self.symbol_Table.search(ctx.ID()[0])
                if (t == False):
                    print("Error: Undeclared variable " + ctx.ID().getText())
                    sys.exit()
                self.file.write("ldo a " + str(t[2]) + "\n")
                self.file.write("ldc i " + ctx.DIGIT().getText() + "\n")
                self.file.write("ixa 1\n")
                self.file.write("ind i\n")
                self.symbol_Table.prev_type=pr
                print(t[0])
                if(pr==t[0]):
                    print("Error: ")
                    sys.exit()
            else:
                t = self.symbol_Table.search(ctx.ID()[0])
                if (t == False):
                    print("Error: Undeclared variable " + ctx.ID().getText())
                    sys.exit()



        if(ctx.DIGIT()!=None):
            if(self.symbol_Table.prev_type != 'int' and self.symbol_Table.prev_type != 'float' and self.symbol_Table.prev_type != 'int*'):
                print("Error: mismatched type, expected " + str(self.symbol_Table.prev_type) + " received int")
                sys.exit()
            else:
                self.file.write("ldc i " + v + "\n")

        if(ctx.STR()!=None):
            if (self.symbol_Table.prev_type != 'char'):
                print("Error: mismatched type, expected " + str(self.symbol_Table.prev_type) + " received char")
                sys.exit()
            else:
                self.file.write("ldc c " + v + "\n")
        if(ctx.FLT()!=None):
            if (self.symbol_Table.prev_type != 'float' ):
                print("Error: mismatched type, expected " + str(self.symbol_Table.prev_type) + " received float")
                sys.exit()
            else:
                self.file.write("ldc r " + v + "\n")
        if(ctx.BOOL()!=None):
            if (self.symbol_Table.prev_type != 'bool'):
                print("Error: mismatched type, expected " + str(self.symbol_Table.prev_type) + " received bool")
                sys.exit()
            else:
                if(v=='false' or v=='0'):
                    v = '0'
                elif(v=='true' or v=='1'):
                    v = '1'
                else:
                    print("Error: ")
                    sys.exit()
                self.file.write("ldc b " + v + "\n")

    def visitLValue(self, ctx:grammarCParser.LValueContext):
        return ctx.getText()
        
    def visitOperation(self, ctx:grammarCParser.OperationContext):
        self.op_state = False
        self.op_prev = None
        if (ctx.operator() != None):
            op = ctx.operator().getText()
            if (self.op_state == True):
                self.visit((ctx.nextOperation())[0])
                self.file.write(self.op_prev + str(self.N) + "\n")
            else:
                self.visit((ctx.nextOperation())[0])
            if (op == "*"):
                self.op_state = True
                self.op_prev = "mull "
                self.visit((ctx.nextOperation())[1])
                if (self.op_state == True):
                    self.file.write(self.op_prev + str(self.N) + "\n")


            elif (op == "/"):
                self.op_state = True
                self.op_prev = "div "
                self.visit((ctx.nextOperation())[1])
                if (self.op_state == True):
                    self.file.write(self.op_prev + str(self.N) + "\n")


            elif (op == "+"):
                self.op_state = False;
                self.visit((ctx.nextOperation())[1])
                if (self.op_state == True):
                    self.file.write(self.op_prev + str(self.N) + "\n")
                self.file.write("add " + str(self.N) + "\n")

            elif (op == "-"):
                self.op_state = False;
                self.visit((ctx.nextOperation())[1])
                if (self.op_state == True):
                    self.file.write(self.op_prev + str(self.N) + "\n")
                self.file.write("sub " + str(self.N) + "\n")

        else:
            self.visitChildren(ctx)

    def visitNextOperation(self, ctx:grammarCParser.NextOperationContext):
        if (ctx.getChildCount() == 1):
            self.visitChildren(ctx)

        elif (ctx.operator() != None):
            op = ctx.operator().getText()
            if (self.op_state == True):
                self.visit(ctx.baseOperation())
                self.file.write(self.op_prev + str(self.N) + "\n")
            else:
                self.visit(ctx.rValue())
            if (op == "*"):
                self.op_state = True
                self.op_prev = "mull "
                self.visit(ctx.nextOperation())


            elif (op == "/"):
                self.op_state = True
                self.op_prev = "div "
                self.visit(ctx.nextOperation())


            elif (op == "+"):
                self.op_state = False;
                self.visit(ctx.nextOperation())
                self.file.write("add " + str(self.N) + "\n")

            elif (op == "-"):
                self.op_state = False;
                self.visit(ctx.nextOperation())
                self.file.write("sub " + str(self.N) + "\n")
        else:
            tempstateSave = self.op_state
            tempOPSave = self.op_prev
            self.op_state = False
            self.visitChildren(ctx)
            if (self.op_state == True):
                self.file.write(self.op_prev + str(self.N) + "\n")
                self.op_state = False
            self.op_state = tempstateSave
            self.op_prev = tempOPSave


    def visitBaseOperation(self, ctx:grammarCParser.BaseOperationContext):
        if(ctx.getChildCount()==1):
            if(ctx.rValue().ID()!=None):
                t = self.symbol_Table.search(ctx.rValue().getText())
                if(t==False):
                    print("Error: " + ctx.rValue().getText() + " is not defined")
                    sys.exit()
            elif(ctx.rValue().FLT()!=None):
                t = ["float"]
            elif(ctx.rValue().DIGIT()!=None):
                t = ["int"]
            else:
                if(ctx.rValue().STR() != None):
                    print("Error: operation not defined for string" )
                elif(ctx.rValue().CHAR() != None):
                    print("Error: operation not defined for char" )
                sys.exit()

            self.N = self.T[t[0]]

            self.visitChildren(ctx)

        elif(ctx.operator()!=None):
            op = ctx.operator().getText()
            if(self.op_state==True):
                self.visit(ctx.rValue())
                self.file.write(self.op_prev + str(self.N) + "\n")
                self.op_state=False
            else:
                self.visit(ctx.rValue())
            if (op == "*"):
                self.op_state = True
                self.op_prev = "mull "
                self.visit(ctx.baseOperation())
                if(ctx.baseOperation().getChildCount()==1 and self.op_state==True):
                    self.file.write(self.op_prev + str(self.N) + "\n")
                    self.op_state=False




            elif (op == "/"):
                self.op_state = True
                self.op_prev = "div "
                self.visit(ctx.baseOperation())
                if(ctx.baseOperation().getChildCount()==1 and self.op_state==True):
                    self.file.write(self.op_prev + str(self.N) + "\n")
                    self.op_state=False

            elif (op == "+"):
                self.op_state = False;
                self.visit(ctx.baseOperation())
                if(ctx.baseOperation().getChildCount()==1 and self.op_state==True):
                    self.file.write(self.op_prev + str(self.N) + "\n")
                    self.op_state=False
                self.file.write("add " + str(self.N) + "\n")

            elif (op == "-"):
                self.op_state = False;
                self.visit(ctx.baseOperation())
                if(ctx.baseOperation().getChildCount()==1 and self.op_state==True):
                    self.file.write(self.op_prev + str(self.N) + "\n")
                    self.op_state=False
                self.file.write("sub " + str(self.N) + "\n")
        else:
            tempstateSave = self.op_state
            tempOPSave = self.op_prev
            self.op_state = False
            self.visitChildren(ctx)
            if (self.op_state == True):
                self.file.write(self.op_prev + str(self.N) + "\n")
                self.op_state = False
            self.op_state = tempstateSave
            self.op_prev = tempOPSave

