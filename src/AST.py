class Node():

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []
        self.data = {}

    def __str__(self):
        return str(self.data)

    def addChild(self, new):
        self.children.append(new)

    def insert(self, key, value):
            #value = (type, function, SP)
        values = self.getData(key)
        if(values[1] != value[1] and values[1] != "function definition"):
            self.data[key] = value
        else:
            print("Error: Duplicate instance of " + str(value[1]))
            raise

    def getData(self, key):
        return self.data.get(key, (0, "error"))

    def getName(self):
        return str(self.name)

    def getParent(self):
        return self.parent

    def getChildren(self):
        return self.children

class AST():

    def __init__(self):
        self.root = None
        self.currentNode = None
        self.depth = 0
        self.file = open('AST.dot', 'w')
        self.id = 0

    def newChild(self, name):
        new = Node(name, self.currentNode)
        if(self.root==None):
            self.root = new
            self.currentNode = self.root

        else:
            self.currentNode.addChild(new)
            self.currentNode = new
            self.depth += 1

    def toParent(self):
        if(self.currentNode!=self.root):
            self.currentNode = self.currentNode.getParent()
            self.depth -= 1

    def toRoot(self):
        self.currentNode = self.root
        self.depth = 0

    def getChild(self, name):
        for i in self.currentNode.children:
            if(str(i.name)==str(name)):
                return i
        return False

    def getNode(self):
        return self.currentNode

    def write(self, node=None):
        if(node==None):
            node = self.root
            self.id = 0
            self.file.write(str(self.id) + "[label=\"" + node.getName() + "\"];\n")

        o_id = self.id

        for i in node.children:
            self.id += 1
            self.file.write(str(self.id) + "[label=\"" + i.getName() + "\"];\n")
            self.file.write(str(o_id) + " -- " + str(self.id) + "\n")
            self.write(i)

    def searchNode(self, name, node=None):
        if(node==None):
            node = self.root
        if(str(node.getName())==str(name)):
            return node
        else:
            for i in node.children:
                x = self.searchNode(name,i)
                if(x!=None):
                    return x

    def getSize(self, name):
        name+='()'
        node = self.searchNode(name)
        s = 0
        if(node!=False):
            for i in node.children:
                if("Def" in str(i.getName()) or "Dcl" in str(i.getName())):
                    s+=1
        return s

    def toDot(self):
        self.write()
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
