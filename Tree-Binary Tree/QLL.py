class Node:
    def __init__(self, nodeValue=None):
        self.nodeValue = nodeValue
        self.next = None

    def __str__(self):
        return str(self.nodeValue)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        currentNode = self.head
        while currentNode:
            yield currentNode
            currentNode = currentNode.next


class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        if self.linkedList.head is None:
            return "Queue is empty"
        else:
            value = [str(x) for x in self.linkedList]
            return ' '.join(value)

    # isEmpty()
    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False

    # enQueue()
    def enQueue(self, enqueueValue):
        newNode = Node(enqueueValue)

        if self.linkedList.head == None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode

        else:
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode

        # return newNode
        # print("The element is inserted at the end of Queue")

    # deQueue()
    def deQueue(self):
        if self.isEmpty():
            return "There is not any element in the Queue to dequeue"
        else:
            firstElement = self.linkedList.head

            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None

            else:
                self.linkedList.head = self.linkedList.head.next
                # print("First Item:: " + str(firstElement) + " is removed.")

            return firstElement

    # peek()
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the Queue to peek"
        else:
            return "Peek value is : " + str(self.linkedList.head)

    # delete the queue
    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None
        print("Entire Queue is Deleted")


# customQueue = Queue()
# # print(customQueue)

# customQueue.enQueue(4)
# customQueue.enQueue(7)
# customQueue.enQueue(9)
# customQueue.enQueue(2)
# print(customQueue)

# customQueue.deQueue()
# print(customQueue)

# customQueue.peek()

# customQueue.delete()
# print(customQueue.isEmpty())
# print(customQueue)
