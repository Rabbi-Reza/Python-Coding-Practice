
class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    # isEmpty()
    def isEmpty(self):
        if self.items == []:
            # print("Queue is Empty")
            return True
        else:
            # print("Queue is not Empty")
            return False

    # Enqueue()
    def enQueue(self, enqueueValue):
        self.items.append(enqueueValue)
        print("The element is inserted at the end of Queue")

    # Dequeue()
    def deQueue(self):
        if self.isEmpty():
            print("There is not any element in the Queue to dequeue")
        else:
            # self.items.pop(0)  # For 0 it will remove first element
            print("First Item:: " + str(self.items.pop(0)) + " is removed.")

    # Peek()
    def peek(self):
        if self.isEmpty():
            print("There is not any element in the Queue to peek")
        else:
            print("Peek value is : " + str(self.items[0]))

    # delete the Queue
    def delete(self):
        self.items = []
        print("Entire Queue is Deleted")


customQueue = Queue()
# print(customQueue.isEmpty())
customQueue.isEmpty()

customQueue.enQueue(4)
customQueue.enQueue(7)
customQueue.enQueue(2)
# print(customQueue.isEmpty())
customQueue.isEmpty()

print(customQueue)

customQueue.deQueue()
print(customQueue)

customQueue.peek()

customQueue.delete()
# print(customQueue.isEmpty())
customQueue.isEmpty()
