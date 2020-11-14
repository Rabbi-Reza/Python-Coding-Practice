
class Queue:
    def __init__(self, maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    # isFull()
    def isFull(self):
        if self.top + 1 == self.start:
            # print("Queue is Full")
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            # print("Queue is Full")
            return True
        else:
            # print("Queue is not Full")
            return False

    # isEmpty()
    def isEmpty(self):
        if self.top == -1:
            # print("Queue is Empty")
            return True
        else:
            # print("Queue is not Empty")
            return False

    # Enqueue()
    def enQueue(self, enqueueValue):
        if self.isFull():
            print("The Queue is Full. No item to enqueue")
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0

            self.items[self.top] = enqueueValue
            print("The element is inserted at the end of Queue")

    # Dequeue()
    def deQueue(self):
        if self.isEmpty():
            print("There is not any element in the Queue to dequeue")
        else:
            firstElement = self.items[self.start]
            start = self.start

            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1

            self.items[start] = None
            print("First Item:: " + str(firstElement) + " is removed.")

    # Peek()
    def peek(self):
        if self.isEmpty():
            print("There is not any element in the Queue to peek")
        else:
            print("Peek value is : " + str(self.items[self.start]))

    # delete the Queue
    def delete(self):
        self.items = self.maxSize * [None]
        self.start = -1
        self.top = -1
        print("Entire Queue is Deleted")


customQueue = Queue(3)

print(customQueue.isFull())
print(customQueue.isEmpty())

customQueue.enQueue(4)
customQueue.enQueue(2)
customQueue.enQueue(7)
print(customQueue)
# customQueue.enqueue(7)

customQueue.deQueue()

print(customQueue)
print(customQueue.isEmpty())

customQueue.peek()
