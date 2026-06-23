class Node:
    def __init__(self, content):
        self.left:Node = None   
        self.right:Node = None
        self.content:str = content
    
class Tree:
    def __init__(self):
        self.root:Node = None
    
    def add(self, content, root = None):
        if self.root is None:
            self.root = Node(content)
            return
        
        if root is None:
            root = self.root
        
        if content > root.content:
            if (root.right is None):
                root.right = Node(content)
            else:
                self.add(content, root.right)
        
        else:
            if (root.left is None):
                root.left = Node(content)
            else:
                self.add(content, root.left)
    
    def printTreeInOrd(self, root = None):
        if root is None:
            root = self.root
        
        if root:
            if root.left:
                self.printTreeInOrd(root.left)
            
            print(root.content)
            
            if root.right:
                self.printTreeInOrd(root.right)

    def printPreOrder(self, root=None):
        """Raiz -> Esquerda -> Direita"""
        if root is None:
            root = self.root
        
        if root:
            print(root.content)
            if root.left: self.printPreOrder(root.left)
            if root.right: self.printPreOrder(root.right)

    def printPostOrder(self, root=None):
        """Esquerda -> Direita -> Raiz"""
        if root is None:
            root = self.root
        
        if root:
            if root.left: self.printPostOrder(root.left)
            if root.right: self.printPostOrder(root.right)
            print(root.content)

tree = Tree()

tree.add("Laura")
tree.add("Diana")
tree.add("Claudiu")
tree.add("Fernando")
tree.add("Rodrigo")
tree.add("Pedro")
tree.printTreeInOrd()
print("------")
tree.printPreOrder()
print("------")
tree.printPostOrder()