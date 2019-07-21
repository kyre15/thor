#This data structure feature is First in First Out (FIFO)

class Queue:

    def __init__(self):
        self.queue = list()

    def addtoq(self, data):
        if data is not None:
            self.queue.insert(0, data)
            return True
        return False

    def size(self):
        return len(self.queue)

    def printqueue(self):
        print(self.queue)

    def remove(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return ("No elements is Queue!")

TQueue = Queue()
TQueue.addtoq("Mon")
TQueue.addtoq("Tue")
TQueue.addtoq("Wed")
TQueue.addtoq("Thu")
print(TQueue.size())
TQueue.printqueue()
print(TQueue.remove())