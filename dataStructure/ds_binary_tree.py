class Node:

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def find(self, data):
        if data < self.data:
            if self.left is None:
                return str(data)+" Not Found"
            return self.left.find(data)
        elif data > self.data:
            if self.right is None:
                return str(data)+" Not Found"
            return self.right.find(data)
        else:
            print(str(self.data) + ' is found')

root = Node(10)
root.insert(6)
root.insert(14)
root.insert(3)
root.printTree()
print("\nUsing find method to find value in Binary tree\n")
print(root.find(7))
print(root.find(14))
