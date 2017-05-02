class Node():

    def __init__(self, id, name, parent):
        self.parent = parent
        self.id = id
        self.name = name

    def getParent(self):
        return self.parent

    def getId(self):
        return self.id

    def getName(self):
        return self.name

class writeAST():

    def __init__(self):
        self.file = open('AST.dot', 'w')
        self.labelnumber = 0
        self.root = None
        self.currentNode = None

    def getNode(self):
        return self.currentNode

    def newNode(self, label):
        self.file.write(str(self.labelnumber) + "[label=\"" + label + "\"];\n")
        self.labelnumber += 1
        return self.labelnumber-1

    def goRoot(self):
            #starts a new child from the root
        self.currentNode = self.root

    def goBack(self):
            #go back to parent
        if(self.currentNode!=self.root):
            self.currentNode = self.currentNode.getParent()

    def newChild(self, label):
        n = self.newNode(label)
        newNode = Node(n,label,self.currentNode)
        self.file.write(str(self.currentNode.getId()) + " -- ")
        self.file.write(str(n) + ";\n")
        self.currentNode = newNode

    def programNode(self):
        self.newNode("program")
        self.root = Node(0, "program", 0)
        self.currentNode = self.root

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
