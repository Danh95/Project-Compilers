class Node():

    def __init__(self, name, parent):
        self.parent = parent
        self.name = name
        self.data = {}

    def __str__(self):
        return str(self.data)

    def insert(self, label, type, function):
        values = self.lookup(label)
        if(values[1]!=function and values[1]!="function definition"):
            self.data[label] = (type, function)
        else:
            print("Error: Duplicate instance of " + str(function))
            raise

    def lookup(self, label):
        return self.data.get(label, (0, "error"))



class symbolTable():

    def __init__(self):
        self.root = None
        self.currentNode = None

    def addChild(self, scopeName):
        n = Node(scopeName, self.currentNode)
        if(self.root == None):
            self.root = n
        self.currentNode = n

    def goToParent(self):
        if(self.currentNode!=self.root):
            self.currentNode = self.currentNode.parent

    def add(self, label, function, type):
            #add in dict
        self.currentNode.insert(label, type, function)

    def search(self, label):
        cN = self.currentNode
        temp = self.currentNode.lookup(label)
        if(temp==(0, "error")):
            self.currentNode = self.currentNode.parent
            if(self.search(label)):
                self.currentNode = cN
                return True
            if (self.currenNode == self.root):
                raise
        else:
            return True