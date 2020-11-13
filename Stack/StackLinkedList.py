
class Node:
    def __init__(self, nodeValue='None'):
        self.nodeValue = nodeValue
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        currentNode = self.head
        while currentNode:
            yield currentNode
            currentNode = currentNode.next


class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        if self.LinkedList.head is None:
            return "Stack is empty"
        else:
            value = [str(x.nodeValue) for x in self.LinkedList]
            return "\n".join(value)

    # isEmpty()
    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False

    # push()
    def push(self, pushValue):
        newNode = Node(pushValue)
        newNode.next = self.LinkedList.head
        self.LinkedList.head = newNode
        print("The element has been successfully inserted")

    # pop()
    def pop(self):
        if self.isEmpty():
            print("There is not any element in the stack")
        else:
            popedNode = self.LinkedList.head.nodeValue
            self.LinkedList.head = self.LinkedList.head.next
            print("Value " + str(popedNode) + " has been deleted")

    # peek()
    def peek(self):
        if self.isEmpty():
            print("There is not any element in the stack")
        else:
            print("Peek value is: " + str(self.LinkedList.head.nodeValue))

    # Delete Stack
    def delete(self):
        self.LinkedList.head = None
        print("Entire Stack deleted")


customStack = Stack()

print(customStack.isEmpty())

customStack.push(3)
customStack.push(1)
customStack.push(7)
customStack.push(5)

# print(customStack.isEmpty())
print(customStack)

customStack.pop()
print(customStack)

customStack.peek()

customStack.delete()
print(customStack)
