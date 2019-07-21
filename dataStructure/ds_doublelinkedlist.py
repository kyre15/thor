class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class doubly_linked_list:

    def __init__(self):
        self.head = None

    def push(self, data):
        NewNode = Node(data)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode

    def printlist(self, node):
        while (node is not None):
            print(node.data)
            last = node
            node = node.next

    def insert(self, prev_node, data):
        if prev_node is None:
            return
        NewNode = Node(data)
        NewNode.next = prev_node.next
        prev_node.next = NewNode
        if NewNode.next is not None:
            NewNode.next.prev = NewNode

    def append(self, data):
        NewNode = Node(data)
        NewNode.next = None
        if self.head is None:
            NewNode.prev = None
            self.head = NewNode
            return
        last = self.head
        while (last.next is not None):
            last = last.next
        last.next = NewNode
        NewNode.prev = last
        return

dlist = doubly_linked_list()
dlist.push("Mon")
dlist.push("Tue")
dlist.push("Wed")
dlist.insert(dlist.head, "Thu")
dlist.printlist(dlist.head)
print("\nappend the value to doubly linked list:")
dlist.append("Sun")
dlist.printlist(dlist.head)
