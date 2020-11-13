class Node:
    def __init__(self, nodeValue=None):
        self.nodeValue = nodeValue
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        currentNode = self.head
        while currentNode:
            yield currentNode
            currentNode = currentNode.next

    # Creation of Doubly Linked List
    def createDLL(self, nodeValue):
        newNode = Node(nodeValue)
        newNode.next = None
        newNode.prev = None

        self.head = newNode
        self.tail = newNode
        return "The DLL is created Successfully"

    # Insertion in Doubly Linked List
    def insertDLL(self, insertValue, Location):
        newNode = Node(insertValue)

        if self.head is None:
            print("The node cannot be inserted")
            # self.head = newNode
            # self.tail = newNode

        else:

            if Location == 0:
                newNode.next = self.head
                newNode.prev = None
                self.head.prev = newNode
                self.head = newNode

            elif Location == -1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode

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

    # Traversal in Doubly Linked List
    def traverseDLL(self):
        if self.head is None:
            print("There is no element to traverse")

        else:
            currentNode = self.head
            while currentNode:
                print(currentNode.nodeValue, end=' ')
                currentNode = currentNode.next
            print()

    def traverseReverseDLL(self):
        if self.head is None:
            print("There is no element to traverse")

        else:
            currentNode = self.tail
            while currentNode:
                print(currentNode.nodeValue, end=' ')
                currentNode = currentNode.prev
            print()

    # Search in Doubly Linked List
    def searchDLL(self, searchValue):
        if self.head is None:
            return "Doubly Linked List does not exist"
        else:
            currentNode = self.head
            index = -1
            while currentNode:
                index += 1
                if currentNode.nodeValue == searchValue:
                    return str(currentNode.nodeValue) + ' at location ' + str(index)
                currentNode = currentNode.next
            return "Search value does not exist in the Linked List"

    # Delete a node in Doubly Linked List
    def deleteNodeDLL(self, Location):
        if self.head is None:
            print("There is not any element in DLL")

        else:
            if Location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None

                else:
                    self.head = self.head.next
                    self.head.prev = None

            elif Location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None

                else:
                    self.tail = self.tail.prev
                    self.tail.next = None

            else:
                currentNode = self.head
                index = 0
                while index < Location - 1:
                    currentNode = currentNode.next
                    index += 1

                currentNode.next = currentNode.next.next
                currentNode.next.prev = currentNode

            print("Successfully Deleted")

    # Delete entire Doubly Linked List
    def deleteEntireDLL(self):
        if self.head is None:
            print("There is not any element in DLL")

        else:
            currentNode = self.head
            while currentNode:
                currentNode.prev = None
                currentNode = currentNode.next

            self.head = None
            self.tail = None
            print("DLL has been successfully deleted")


DLL = DoublyLinkedList()
DLL.createDLL(1)

DLL.insertDLL(2, 0)
DLL.insertDLL(4, 0)
DLL.insertDLL(5, -1)
DLL.insertDLL(8, 2)

print([node.nodeValue for node in DLL])

DLL.traverseDLL()
DLL.traverseReverseDLL()

print(DLL.searchDLL(5))

print([node.nodeValue for node in DLL])

DLL.deleteNodeDLL(2)
print([node.nodeValue for node in DLL])

DLL.deleteNodeDLL(0)
print([node.nodeValue for node in DLL])

DLL.deleteNodeDLL(-1)
print([node.nodeValue for node in DLL])

DLL.deleteEntireDLL()
print([node.nodeValue for node in DLL])
