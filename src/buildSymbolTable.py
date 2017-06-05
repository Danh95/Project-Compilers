from grammar.grammarCVisitor import grammarCVisitor
from grammar.grammarCParser import grammarCParser
from symbolTable import symbolTable
from AST import AST
import sys

class buildSymbolTable(grammarCVisitor):

    def __init__(self, AST, filename):
        self.ast = AST
        self.symbol_Table = symbolTable()
        self.SP = 4
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
        self.scf = 0

        self.MP = 1
        self.return_type = None

        self.inDef = False

        self.arrayS = 0


    def visitProgram(self, ctx:grammarCParser.ProgramContext):
        self.symbol_Table.addChild("Program")
        self.file.write("ssp 4\n")
        self.file.write("ujp global\n")
        self.visitLibraryList(ctx.libraryList())
        if(ctx.globalList()!=None):
            self.file.write("global:\n")
            self.visitGlobalList((ctx.globalList()))
            self.file.write("ujp start\n")
        self.visitFuncDefList(ctx.funcDefList())
        self.symbol_Table.goToParent()

    def visitLibname(self, ctx:grammarCParser.LibnameContext):
        if(ctx.getText()=='stdio'):
            self.symbol_Table.add("scanf", "function definition", 'int')
            self.file.write("scanfd:\nin i\nsto i\nretp\n")
            self.file.write("scanfi:\nin i\nsto i\nretp\n")
            self.file.write("scanfc:\nin c\nsto c\nretp\n")
            self.file.write("scanfs:\n")
            for i in range(0,15):
                self.file.write("ldc c 0\n")
            self.file.write("ldc c 27\n")
            self.file.write("inscanfs:\nin c\ndpl c\nldc c 27\nequ c\nfjp s\nsto c\nretp\ns:\nsto c\ninc a 1\nujp inscanfs\n")
            #scanfs voor string met array
            self.symbol_Table.add("printf", "function definition", 'int')
            self.file.write("printfd:\nout i\nretp\n")
            self.file.write("printfi:\nout i\nretp\n")
            self.file.write("printfc:\nout c\nretp\n")

            self.file.write("printfs:\ninprintfs:\ninc a 1\ndpl c\nind c\nldc c 27\nequ c\nfjp p\nretp\n")
            self.file.write("p:\nout c\nujp inprintfs\n")


    def visitMainFunc(self, ctx:grammarCParser.MainFuncContext):
        self.return_type = 'int'
        self.symbol_Table.add("Main", "mainfunction", ctx.getChild(0).getText())
        self.symbol_Table.addChild("Main")
        if(ctx.getChildCount()!=0):
            self.file.write("start:\n")
        self.visitChildren(ctx)
        self.file.write("hlt\n")
        self.symbol_Table.goToParent()

    def visitFuncDef(self, ctx:grammarCParser.FuncDefContext):
        self.return_type = ctx.types().getText()
        name = self.visitLValue(ctx.lValue())
        if(ctx.argList()!=None):
            typelist = ctx.argList().types()
            tn = []
            for i in range(0, ctx.argList().getChildCount()):
                if(ctx.argList().getChild(i) in typelist):
                    tn.append(ctx.argList().getChild(i).getText())
                    if(i+2<ctx.argList().getChildCount()):
                        if(ctx.argList().getChild(i+2).getText()!=','):
                            tn=tn[:-1]
                            tn.append("array")
            for i in tn:
                name+=str(i)
        self.symbol_Table.add(name, "function definition", self.visitTypes(ctx.types()))
        self.symbol_Table.addChild(name)
        self.SP += len(ctx.argList().types())+4
        self.file.write(ctx.lValue().getText() +":\n")
        stackP = self.SP
        self.file.write("ssp "+ str(len(ctx.argList().lValue())+6) + "\n")
        storage_size = self.ast.getSize(ctx.lValue().getText())
        self.file.write("sep " + str(storage_size) + "\n")
        self.visitChildren(ctx)
            #do something to return
        self.SP = stackP
        self.file.write("retp\n")
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
                    #self.SP

    def visitDeclaration(self, ctx:grammarCParser.DeclarationContext):
        if(ctx.arrayDecl()==None):
            name = self.visitLValue(ctx.lValue())
            s = self.symbol_Table.search(ctx.lValue().getText())
            if(s!=False):
                if(s[3]==0):
                    print("Error: Redeclaration of " + ctx.lValue().getText())
                    sys.exit()
            t = ctx.types().getText()
            if(ctx.pointer()!=[]):
                for i in ctx.pointer():
                    t += '*'
                self.file.write("ldc " + str(self.T["pointer"]) + " " + str(self.SP+1) + "\n")


            else:
                tp = str(self.T[t])
                n = "0"
                if(tp=='r'):
                    n="0.0"
                elif(tp=='b'):
                    n="f"

                self.file.write("ldc " + tp + " " + n +"\n")
            self.symbol_Table.add(name, "var declaration", t, self.SP)
            self.SP += 1
        else:
            self.visitArrayDecl(ctx.arrayDecl())

        self.symbol_Table.resetType()

    def visitArrayDecl(self, ctx:grammarCParser.ArrayDeclContext):
        name = self.visitLValue(ctx.lValue())
        s = self.symbol_Table.search(ctx.lValue().getText())
        if(s != False):
            if(s[3]==0):
                print("Error: Redeclaration of " + ctx.lValue().getText())
                sys.exit()
        t = 'array'
        self.symbol_Table.add(name, ctx.types().getText(), t, self.SP, int(ctx.DIGIT().getText()))
        self.file.write("ldc a " + str(self.SP+1) + "\n")
        self.SP += 1
        if(ctx.DIGIT()!=None):
            for i in range(0, int(ctx.DIGIT().getText())):
                tp = str(self.T[ctx.types().getText()])
                n = "0"
                if (tp == 'r'):
                    n = "0.0"
                elif (tp == 'b'):
                    n = "f"
                self.file.write("ldc "+ tp + " " + n + "\n")
                self.SP += 1

        else:
            print("Error: array index not validatable")
            sys.exit()

        self.SP += 1
    def visitDefinition(self, ctx:grammarCParser.DefinitionContext):
        self.inDef = True
        if(ctx.assignment().normalAssignment()!=None):
            name = ctx.assignment().normalAssignment().lValue().getText()
            st = self.symbol_Table.search(name)
            if(st!=False):
                if(st[3]==0):
                    print("Error: Redefinition of " + name)
                    sys.exit()
            t = ctx.types().getText()
            if (ctx.pointer() != []):
                for i in ctx.pointer():
                    t += '*'
                self.file.write("ldc " + str(self.T["pointer"]) + " " + "0\n")
            else:
                tp = str(self.T[t])
                n = "0"
                if (tp == 'r'):
                    n = "0.0"
                elif (tp == 'b'):
                    n = "f"
                self.file.write("ldc " + tp + " " + n +"\n")
            self.symbol_Table.add(name, "var definition", t, self.SP)
            #self.SP+=1
            self.visitAssignment(ctx.assignment())
        else:
            name = ctx.assignment().arrayAssignment().lValue().getText()
            s = self.symbol_Table.search(name)
            if(s!=False):
                if(s[3]==0):
                    print("Error: Redefinition of " + name)
                    sys.exit()
            if(ctx.assignment().arrayAssignment().ID()!=None):
                print("Error: variable array size")
                sys.exit()
            self.symbol_Table.add(name, ctx.types().getText(), 'array', self.SP, int(ctx.assignment().arrayAssignment().DIGIT().getText()))
            #self.file.write("ldc " + str(self.T[ctx.types().getText()]) + " 0\n")
            #self.SP += 1

            self.file.write("ldc a " + str(self.SP+1) + "\n")
            self.SP += 1
            self.visitChildren(ctx)

        self.inDef = False

    def visitFunctionCall(self, ctx:grammarCParser.FunctionCallContext):
        name = ctx.lValue().getText()
        arg = ctx.parList().rValue()
        stdio = {'s' : 'char*', 'd' : 'int', 'i' : 'int', 'c' : 'char'}
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
                            self.file.write("ldc c \'\\'\n")
                            i += 1

                        else:

                            self.file.write("ldc c " + "\'" + str(string[i]) + "\'\n")
                        self.file.write("out c\n")
                i+=1
            if(len(speci)!=(len(arg)-1)):
                print("Error: incorrect number of specifiers")
                sys.exit()
            for i in arg[1:]:
                if(i.ID()!=[]):
                    var = i.ID()[0].getText()

                else:
                    var = i.getText()

                t = speci.pop(0)
                var.replace("*", "")
                var.replace("&", "")
                entry = self.symbol_Table.search(var)
                if(len(i.ID())==2 or (i.ID()!=[] and i.DIGIT()!=None)):
                    entry = (entry[1], entry[0], entry[2], entry[3], entry[4])
                if(entry==False):
                    print("Error: " + i.getText() + " does not exist")
                    sys.exit()
                else:
                    #type check
                    if(entry[0]!=stdio[t]):
                        print("Error: specifier does not match variable")
                        sys.exit()

                if(name=='scanf'):
                    slabel = scanf_d[t]
                    if(slabel=="scanfs"):
                        self.file.write("mst 0\n")
                        self.file.write("ldc a " + str(entry[2]) + "\n")
                        self.file.write("ldc a " + str(self.SP) + "\n")
                        self.file.write("sto a\n")
                        self.file.write("cup 1 scanfs\n")
                    else:
                        self.file.write("mst 0\n")
                        self.file.write("ldc a " + str(entry[2]) + "\n")
                        self.file.write("cup 1 " + slabel + "\n")
                else:
                    self.file.write("mst 0\n")
                    self.visitRValue(i)
                    self.file.write("cup 1 " + printf_d[t] + "\n")



        else:
            temp_MP = self.MP
            pt = None
            if(self.symbol_Table.prev_type!=None):
                pt = self.symbol_Table.prev_type
            for i in arg:
                if(i.ID()!=None and i.ID()!=[]):
                    s = self.symbol_Table.search(i.getText())
                    self.symbol_Table.resetType()
                    if(s==False):
                        print("Error: argument not defined")
                        sys.exit()
                    name += str(s[0])
                elif(i.DIGIT()!=None):
                    name += 'int'
                elif (i.BOOL() != None):
                    name += 'bool'
                elif (i.STR() != None):
                    name += 'char'
                elif (i.FLT() != None):
                    name += 'float'

            self.symbol_Table.prev_type=pt
            st = self.symbol_Table.search(name)
            self.symbol_Table.resetType()
            if(st==False):
                print("Error: Function called before definition, unvalid reference to " + ctx.lValue().getText())
                sys.exit()
            self.MP = self.SP+1
            self.file.write("mst " + str(st[3]) + "\n")
            self.visit(ctx.parList())
                #storage requirement for parameters

            self.file.write("cup " + str(len(arg)) + " "+ ctx.lValue().getText() + "\n")

            self.MP = temp_MP

    def visitEndStatement(self, ctx:grammarCParser.EndStatementContext):
        self.symbol_Table.resetType()
        self.visitChildren(ctx)

    def visitNormalAssignment(self, ctx:grammarCParser.NormalAssignmentContext):
        self.symbol_Table.resetType()
        t = self.symbol_Table.search(ctx.lValue().getText())
        if(t==False):
            print("Error: Assignment before declaration, unvalid reference to " + ctx.lValue().getText())
            sys.exit()
        if(t[0]=='array'):
            print("Error: incorrect assignment to array")
            sys.exit()
        self.file.write("ldc a " + str(t[2]) + "\n")
        self.visitChildren(ctx)
        if((t[0])[-1]=="*"):
            self.file.write("sto a \n")
        else:
            self.file.write("sto " + str(self.T[t[0]]) + "\n")

    def visitArrayAssignment(self, ctx:grammarCParser.ArrayAssignmentContext):
        self.symbol_Table.resetType()
        t=self.symbol_Table.search(ctx.lValue().getText())
        if(t==False):
            print("Error: Assignment before declaration, invalid reference to " + ctx.lValue().getText())
            sys.exit()

        if(self.inDef):
            #part of definition
            if(ctx.DIGIT()==None):
                print("Error: array index not validatable")
                sys.exit()
            self.arrayS = int(ctx.DIGIT().getText())
            #self.file.write("ldc a " + str(t[2]) + "\n")
            self.symbol_Table.prev_type=t[1]
            self.visitChildren(ctx)
        else:
            #assign 1 value to a place in the array
            if(ctx.DIGIT()!=None):
                self.file.write("ldc i " + str(ctx.DIGIT().getText()) + "\n")
                self.arrayS = int(ctx.DIGIT().getText())
            elif(ctx.ID() != None):
                s = self.symbol_Table.search(ctx.ID[1]().getText())
                self.file.write("ldo i " + str(s[2]) + "\n")
                self.arrayS = int(s[4])

            else:
                print("Error: index not an integer")
                sys.exit()
            self.file.write("ldo a " + str(t[2]) + "\n")
            self.file.write("ixa 1\n")
            self.symbol_Table.prev_type=t[1]
            self.visitChildren(ctx)
            self.file.write("sto " +str(self.T[t[1]]) + "\n")


    def visitArrayOptions(self, ctx:grammarCParser.ArrayOptionsContext):
        if(self.inDef==False):
            #assignment of x[2]=y[2] or x[2]=y(not possible if y array)
            if (ctx.getChildCount() != 1):
                print("Error: incorrect assignment of array")
                sys.exit()
            else:
                self.visitChildren(ctx)


        else:
            #definition of int x[5]=...
            if (ctx.getChildCount() == 1):
                #=b(not possible) or =b[2](not possible)
                print("Error: incorrect definition of array")
                sys.exit()
            elif (ctx.getChildCount()==2):
                for i in range(0, self.arrayS):
                    self.file.write("ldc i 0\n")
                    self.SP += 1
            elif (ctx.getChildCount()>=3):
                #={...}
                if(len(ctx.rValue())!=self.arrayS):
                    print("Error: initializer list doesn't match array size")
                    sys.exit()
                else:
                    for i in range(0, self.arrayS):
                        self.visitRValue(ctx.rValue()[i])
                    self.SP += self.arrayS

    def visitConditional(self, ctx:grammarCParser.ConditionalContext):
        self.ec+=1
        var_ec = self.ec
        self.visitChildren(ctx)
        self.file.write("endCond" + str(var_ec) + ":\n")

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
        self.file.write("ujp l" + str(self.lc) + "\nl" + str(self.lc) + ":\n")
        var_lc = self.lc
        self.lc += 1
        self.visitCondition(ctx.condition())
        self.file.write("fjp endCond" + str(self.ec) + "\n")
        self.visitBody(ctx.body())
        self.file.write("ujp l" + str(var_lc) + "\n")
        self.symbol_Table.goToParent()

    def visitLoop(self, ctx:grammarCParser.WhileStatementContext):
        self.symbol_Table.addChild("if")
        self.visitForCondition(ctx.forCondition())
        self.visitBody(ctx.body())
        self.symbol_Table.goToParent()

    def visitCondition(self, ctx:grammarCParser.ConditionContext):
        DC = {'<' : 'les', '>' : 'grt', '==' : 'eq', '>=' : 'geq', '<=' : 'leq', '!=' : 'neq'}
        if(ctx.comparison()!=None):
            type1 = None;
            type2 = None;
            if((ctx.rValue())[0].ID()!=[]):
                type1 = (self.symbol_Table.search((ctx.rValue())[0].getText()))
            if((ctx.rValue())[1].ID()!=[]):
                type2 = (self.symbol_Table.search((ctx.rValue())[1].getText()))
            if(type1==False or type2==False):
                print("Error: argument not declared before comparison")
                sys.exit()
            if ((ctx.rValue())[0].ID() != [] and (ctx.rValue())[1].ID() != []):
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
                self.file.write("ldc b t\nneq b\n")
                self.SP += 1

            elif(ctx.getChildCount()==2):
                if ((ctx.rValue())[0].DIGIT() != None or (ctx.rValue())[0].BOOL() != None):
                    if ((ctx.rValue())[0].getText() == "0"):
                        self.file.write("ldc b t\n")
                    else:
                        self.file.write("ldc b f\n")
                    self.SP += 1

                else:
                    print("ERROR: unsupported type for comparison")
                    sys.exit()
            elif(ctx.getChildCount()==1):
                if((ctx.rValue())[0].DIGIT()!=None or (ctx.rValue())[0].BOOL()!=None):
                    if((ctx.rValue())[0].getText()=="0"):
                        self.file.write("ldc b f\n")
                    else:
                        self.file.write("ldc b t\n")
                    self.SP += 1

                else:
                    print("ERROR: unsupported type for comparison")
                    sys.exit()



    def visitRValue(self, ctx:grammarCParser.RValueContext):
        v = ctx.getText()
        array = False
        if(ctx.ID()!=[]):


            if(len(ctx.ID())==2):
                pr = self.symbol_Table.prev_type
                self.symbol_Table.prev_type = "array"
                t = self.symbol_Table.search(ctx.ID()[0])
                if (t == False):
                    print("Error: Undeclared variable " + ctx.ID().getText())
                    sys.exit()
                t = (t[1], t[0], t[2], t[3], t[4])
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

                if((pr!=t[0] and t[1]!="array") or (pr!=t[1] and t[0]!="array")):
                    print("Error: type mismatched")
                    sys.exit()
                array=True

            elif(ctx.DIGIT()!=None):
                pr = self.symbol_Table.prev_type
                self.symbol_Table.prev_type="array"
                t = self.symbol_Table.search(ctx.ID()[0])
                if (t == False):
                    print("Error: Undeclared variable " + ctx.ID()[0].getText())
                    sys.exit()
                t = (t[1], t[0], t[2], t[3])
                self.file.write("ldo a " + str(t[2]) + "\n")
                self.file.write("ldc i " + ctx.DIGIT().getText() + "\n")
                self.file.write("ixa 1\n")
                self.file.write("ind i\n")
                self.symbol_Table.prev_type=pr
                if((pr!=t[0] and t[1]!="array") or (pr!=t[1] and t[0]!="array")):
                    print("Error: type mismatched")
                    sys.exit()
                array = True
            else:
                t = self.symbol_Table.search(ctx.ID()[0])
                if (t == False):
                    print("Error: Undeclared variable " + ctx.ID().getText())
                    sys.exit()
                if (str(t[0])=='array'):
                    print("Error: array as RValue")
                    sys.exit()

            if(ctx.pointer()!=[]):
                for i in ctx.pointer():
                    self.symbol_Table.prev_type+="*"
            elif(ctx.reference()!=[]):
                for i in ctx.reference():
                    if(self.symbol_Table.prev_type[-1]=="*"):
                        self.symbol_Table.prev_type=self.symbol_Table.prev_type[:-1]
                    else:
                        print("Error: Unexpected pointer type")
                        sys.exit()


            else:
                if(array==False):
                    self.file.write("ldc a " + str(t[2]) + "\n")
                    if (ctx.pointer() != []):
                        for i in ctx.pointer():
                            self.file.write("ind a\n")
                    elif (ctx.reference() != []):
                        self.file.write("ldo a " + str(t[2]) + "\n")
                        for i in range(0,len(ctx.reference())-1):
                            self.SP+=1
                            self.file.write("ldo a " + str(self.SP-1) + "\n")
                    if(self.T.get(self.symbol_Table.prev_type, (0, "error"))!=(0, "error")):
                        self.file.write("ind " + str(self.T[t[0]]) + "\n")
                    else:
                        self.file.write("ind a\n")


        if(ctx.DIGIT()!=None and ctx.ID()==[]):
            if(self.symbol_Table.prev_type != 'int' and self.symbol_Table.prev_type != 'float' and self.symbol_Table.prev_type != 'int*' and self.symbol_Table.prev_type !=None):
                print("Error: mismatched type, expected " + str(self.symbol_Table.prev_type) + " received int")
                sys.exit()
            else:
                self.file.write("ldc i " + v + "\n")

        if(ctx.STR()!=None):
            if (self.symbol_Table.prev_type != 'char' and self.symbol_Table.prev_type!=None):
                print("Error: mismatched type, expected " + str(self.symbol_Table.prev_type) + " received char")
                sys.exit()
            else:
                self.file.write("ldc c " + v + "\n")
        if(ctx.FLT()!=None):
            if (self.symbol_Table.prev_type != 'float' and self.symbol_Table.prev_type!=None):
                print("Error: mismatched type, expected " + str(self.symbol_Table.prev_type) + " received float")
                sys.exit()
            else:
                self.file.write("ldc r " + v + "\n")
        if(ctx.BOOL()!=None):
            if (self.symbol_Table.prev_type != 'bool' and self.symbol_Table.prev_type!=None):
                print("Error: mismatched type, expected " + str(self.symbol_Table.prev_type) + " received bool")
                sys.exit()
            else:
                if(v=='false' or v=='0'):
                    v = 'f'
                elif(v=='true' or v=='1'):
                    v = 't'
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
                self.op_prev = "mul "
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
                self.op_prev = "mul "
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
            if(ctx.rValue().ID()!=[]):
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
                self.op_prev = "mul "
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

    def visitReturnStatement(self, ctx:grammarCParser.ReturnStatementContext):
        self.symbol_Table.prev_type=self.return_type
        self.visitChildren(ctx)
        if(ctx.getChild(1)==ctx.endStatement()):
            self.file.write("retp\n")

        else:
            self.file.write("sro " + str(self.T[str(self.return_type)]) + " " + str(self.MP) + "\nretf\n")

