import sys

class Node():

    def __init__(self, name, parent):
        self.parent = parent
        self.name = name
        self.data = {}

    def __str__(self):
        return str(self.data)

    def insert(self, label, type, function, SP):
        values = self.lookup(label)
        if(values[1]!=function and values[1]!="function definition"):
            self.data[label] = (type, function, SP)
        else:
            print("Error: Duplicate instance of " + str(function))
            raise

    def lookup(self, label):
        #when new definition or declaration
        return self.data.get(label, (0, "error"))



class symbolTable():

    def __init__(self):
        self.root = None
        self.currentNode = None
        self.prev_type = None


    def addChild(self, scopeName):
        n = Node(scopeName, self.currentNode)
        if(self.root == None):
            self.root = n
        self.currentNode = n

    def goToParent(self):
        if(self.currentNode!=self.root):
            self.currentNode = self.currentNode.parent

    def add(self, label, function, type, SP=None):
            #add in dict
        self.currentNode.insert(label, type, function, SP)

    def resetType(self):
        self.prev_type=None

    def search(self, label):
        #when operation on existing variable or functioncall
        cN = self.currentNode
        #print(label)
        temp = self.currentNode.lookup(str(label))
        #print(temp)
        if(temp==(0, "error")):
            #not found in current Node
            self.currentNode = self.currentNode.parent
            if (self.currentNode == self.root):
                self.currentNode = cN
                print(cN)
                return False

            if(self.search(str(label))!=False):
                self.currentNode = cN
                print(cN)
                return temp
            else:
                self.currentNode = cN
                print(cN)
                return False

        else:
            #found
            if(self.prev_type!=None):
                if(temp[0]==self.prev_type):
                    return temp
                else:
                    print("Error: type mismatched" )
                    sys.exit()
                    

            else:
                self.prev_type = temp[0]
                return temp