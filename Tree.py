class Node:

    def __init__(self, content):
        self.left = None
        self.right = None
        self.content = content


class Tree:

    def __init__(self, key):
        self.root = None
        self.key = key   # atributo usado para comparar


    def add(self, content, root=None):

        if self.root is None:
            self.root = Node(content)
            return

        if root is None:
            root = self.root


        if self.key(content) > self.key(root.content):

            if root.right is None:
                root.right = Node(content)
            else:
                self.add(content, root.right)


        else:

            if root.left is None:
                root.left = Node(content)
            else:
                self.add(content, root.left)



    def search(self, value, root=None):

        if root is None:
            root = self.root

        if root is None:
            return None


        if self.key(root.content) == value:
            return root.content


        if value < self.key(root.content):
            return self.search(value, root.left)

        return self.search(value, root.right)



    def inOrder(self, root=None):

        if root is None:
            root = self.root
            if root is None:
                return


        if root.left:
            self.inOrder(root.left)


        print(root.content)


        if root.right:
            self.inOrder(root.right)



    def reverseOrder(self, root=None):

        if root is None:
            root = self.root
            if root is None:
                return


        if root.right:
            self.reverseOrder(root.right)


        print(root.content)


        if root.left:
            self.reverseOrder(root.left)



    def remove(self, value, root=None):

        if root is None:
            root = self.root


        if value < self.key(root.content):

            root.left = self.remove(value, root.left)


        elif value > self.key(root.content):

            root.right = self.remove(value, root.right)


        else:


            if root.left is None:
                return root.right


            if root.right is None:
                return root.left


            aux = root.right

            while aux.left:
                aux = aux.left


            root.content = aux.content

            root.right = self.remove(
                self.key(aux.content),
                root.right
            )
        return root