class BinaryTree(object):
    def __init__(self,new):
        self.root=new
        self.LeftNode=None
        self.RightNode=None
    def insertLeft(self,newNode):
        if self.LeftNode==None:
            self.leftNode=BinaryTree(newNode)
        else:
            t=self.LeftNode
            self.leftNode=BinaryTree(newNode)
            slef.leftNode.leftNode=t
    def insertRight(self,newNode):
        if self.RightNode==None:
            self.RightNode=BinaryTree(newNode)
        else:
            t=self.RightNode
            self.RightNode=BinaryTree(newNode)
            slef.RightNode.RightNode=t
    def getLeftNode(self):
        return self.LeftNode
    def getRightNode(self):
        return self.RightNode
    def setRoot(self,obj):
        self.root=obj
    def getRoot(self):
        return self.root


rajnish dwivedy <rajnishdwivedy@gmail.com>
Jan 11
to me 
class BinaryTree(object):
    def __init__(self,new):
        self.root=new
        self.LeftNode=None
        self.RightNode=None
    def insertLeft(self,newNode):
        if self.LeftNode==None:
            self.LeftNode=BinaryTree(newNode)
        else:
            t=self.LeftNode
            self.LeftNode=BinaryTree(newNode)
            slef.LeftNode.leftNode=t
    def insertRight(self,newNode):
        if self.RightNode==None:
            self.RightNode=BinaryTree(newNode)
        else:
            t=self.RightNode
            self.RightNode=BinaryTree(newNode)
            slef.RightNode.RightNode=t
    def getLeftNode(self):
        return self.LeftNode
    def getRightNode(self):
        return self.RightNode
    def setRoot(self,obj):
        self.root=obj
    def getRoot(self):
        return self.root
    def preOrder(self):
        print(self.root)
        if self.LeftNode!=None:
            self.LeftNode.preOrder()
        if self.RightNode!=None:
            self.RightNode.preOrder()
    def postOrder(self):
        if self.LeftNode!=None:
            self.LeftNode.postOrder()
        if self.RightNode!=None:
            self.RightNode.postOrder()
        print(self.root)
    def InOrder(self):
        if self.LeftNode!=None:
            self.LeftNode.InOrder()
        print(self.root)    
        if self.RightNode!=None:
            self.RightNode.InOrder()
