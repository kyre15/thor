class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def listprint(self):
        printlist = self.head
        while printlist is not None:
            print(printlist.data)
            printlist = printlist.next

    def AddatBegining(self,newdata):
        NewNode = Node(newdata)
        NewNode.next = self.head
        self.head = NewNode

list = LinkedList()
list.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
list.head.next = e2
e2.next = e3
list.listprint()

list.AddatBegining("Sun")
print("\nAdd new head")
list.listprint()