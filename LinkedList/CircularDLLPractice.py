
class Node:
    def __init__(self, nodeValue=None):
        self.nodeValue = nodeValue
        self.next = None
        self.prev = None


class CircularDLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        currentNode = self.head
        while currentNode:
            yield currentNode
            if currentNode.next == self.head:
                break
            currentNode = currentNode.next

    # Creation of Circular Doubly Linked List
    def createCDLL(self, nodeValue):
        newNode = Node(nodeValue)

        self.head = newNode
        self.tail = newNode
        newNode.next = newNode
        newNode.prev = newNode

        return "The Circular DLL is created Successfully"

    # Insertion in Circular Doubly Linked List
    def insertCDLL(self, insertValue, Location):
        if self.head is None:
            print("There is not any element in CDLL")

        else:
            newNode = Node(insertValue)

            if Location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.tail.next = newNode
                self.head.prev = newNode
                self.head = newNode

            elif Location == -1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
                self.head.prev = newNode

            else:
                currentNode = self.head
                index = 0
                while index < Location - 1:
                    currentNode = currentNode.next
                    index += 1

                newNode.next = currentNode.next
                newNode.prev = currentNode
                currentNode.next = newNode
                newNode.next.prev = newNode

    # Traverse in Circular Doubly Linked List
    def traverseCDLL(self):
        if self.head is None:
            print("Circular Doubly Linked List does not exist")
        else:
            currentNode = self.head
            while currentNode:
                print(currentNode.nodeValue, end=' ')
                if currentNode.next == self.head:
                    break
                currentNode = currentNode.next
            print()

    def traverseReverseCDLL(self):
        if self.head is None:
            print("Circular Doubly Linked List does not exist")
        else:
            currentNode = self.tail
            while currentNode:
                print(currentNode.nodeValue, end=" ")
                if currentNode.prev == self.tail:
                    break
                currentNode = currentNode.prev
            print()

    # Search in Circular Doubly Linked List
    def searhCDLL(self, searchValue):
        if self.head is None:
            print("Circular Doubly Linked List does not exist")

        else:
            currentNode = self.head
            index = 0
            while currentNode:
                if currentNode.nodeValue == searchValue:
                    return str(currentNode.nodeValue) + ' at location ' + str(index)
                if currentNode.next == self.head:
                    break
                currentNode = currentNode.next
                index += 1
            return "Search value does not exist in the Linked List"

    # Delete a node in Circular Doubly Linked List
    def deleteNodeCDLL(self, Location):
        if self.head is None:
            print("There is not any element in CDLL")
        else:
            if Location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head.prev = None
                    self.head = None
                    self.tail = None

                else:
                    self.tail.next = self.head.next
                    self.head = self.head.next
                    self.head.prev = self.tail

            elif Location == -1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head.prev = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail

            else:
                currentNode = self.head
                index = 0
                while index < Location - 1:
                    if currentNode.next == self.head:
                        break
                    currentNode = currentNode.next
                    index += 1

                currentNode.next = currentNode.next.next
                currentNode.next.prev = currentNode

            print("Successfully Deleted a node from CDLL")

    # Delete a node in Circular Doubly Linked List
    def deleteEntireCDLL(self):
        if self.head is None:
            print("There is not any element in DLL")

        else:
            currentNode = self.head
            while currentNode:
                if currentNode.next == self.head:
                    break
                currentNode.prev = None
                currentNode = currentNode.next
            self.head = None
            self.tail = None
            print("Successfully Deleted Entire CDLL")


CDLL = CircularDLL()
print(CDLL.createCDLL(3))

print([node.nodeValue for node in CDLL])

CDLL.insertCDLL(2, 0)
CDLL.insertCDLL(4, 0)
CDLL.insertCDLL(5, -1)
CDLL.insertCDLL(8, 2)

print([node.nodeValue for node in CDLL])

CDLL.traverseCDLL()
CDLL.traverseReverseCDLL()

print(CDLL.searhCDLL(2))

print([node.nodeValue for node in CDLL])

CDLL.deleteNodeCDLL(0)
print([node.nodeValue for node in CDLL])
CDLL.deleteNodeCDLL(-1)
print([node.nodeValue for node in CDLL])
CDLL.deleteNodeCDLL(2)
print([node.nodeValue for node in CDLL])

CDLL.deleteEntireCDLL()
print([node.nodeValue for node in CDLL])
