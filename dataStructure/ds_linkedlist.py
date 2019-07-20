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

    def AddatBeginning(self,newdata):
        NewNode = Node(newdata)
        NewNode.next = self.head
        self.head = NewNode

    def Addattheend(self,newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            return
        laste = self.head
        while(laste.next):
            laste = laste.next
        laste.next = NewNode

    def Inbetween(self, middle_node, newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return
        NewNode = Node(newdata)
        NewNode.next = middle_node.next
        middle_node.next = NewNode

    def RemoveNode(self, Removekey):

        headVal = self.head

        if (headVal is not None):
            if (headVal.data == Removekey):
                self.head = headVal.next
                headVal = None
                return

        while (headVal is not None):
            if headVal.data == Removekey:
                break
            prev = headVal
            headVal = headVal.next

        if (headVal == None):
            return

        prev.next = headVal.next

        headVal = None

list = LinkedList()
list.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
list.head.next = e2
e2.next = e3
list.listprint()

list.AddatBeginning("Sun")
print("\nAdd new head")
list.listprint()

list.Addattheend("Thu")
print("\nAdd new end")
list.listprint()

list.Inbetween(list.head.next, "Fri")
print("\nAdd new value in between")
list.listprint()

list.RemoveNode("Thu")
print("\nRemove Thu from the list:")
list.listprint()