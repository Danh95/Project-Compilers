class writeAST():

    def __init__(self):
        self.file = open('AST.dot', 'w')
        self.labelnumber = 0
        self.currentNode = 0

    def newNode(self, label):
        self.file.write(str(self.labelnumber) + "[label=\"" + label + "\"];\n")
        self.labelnumber += 1
        return self.labelnumber-1

    def newStatement(self):
            #starts a new child from the root == a new statement
        self.currentNode = 0

    def noChild(self):
        self.currentNode -= 1

    def newChild(self, label):
        n = self.newNode(label)
        self.file.write(str(self.currentNode) + " -- ")
        self.file.write(str(n) + ";\n")
        self.currentNode = n

    def programNode(self):
        self.newNode("program")



    def convertFile(self):
        self.file.close()
        f = open('AST.dot', 'r')
        graph = f.read()

        f.close()
        open('AST.dot', 'w').close()
        f = open('AST.dot', 'w')
        f.write("graph AST {\n")
        f.write(graph)
        f.write("\n}")
        f.close()
