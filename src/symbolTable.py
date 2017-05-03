class Node():

    def __init__(self, name, parent):
        self.parent = parent
        self.name = name
        self.data = {}

    def insert(self, label, type):
        self.data[label] = type

    def lookup(self, label):
        pass

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
        self.currentNode.insert(label, type)