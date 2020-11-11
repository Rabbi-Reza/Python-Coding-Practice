#  Create Circular Linked List
class Node:
    def __init__(self, nodeValue=None):
        self.nodeValue = nodeValue
        self.next = None


class CircularLinkedList():
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
            # currentNode = currentNode.next
            # if currentNode == self.tail.next:
            #     break

    #  Creation of circular singly linked list
    def createSLL(self, nodeValue):
        node = Node(nodeValue)

        node.next = node
        self.head = node
        self.tail = node

        return 'Circular Singly Linked List Created'

    #  Insertion of a node in circular singly linked list
    def insertCSLL(self, nodeValue, location):
        newNode = Node(nodeValue)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode
            return "The head reference is None"

        else:

            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode

                location = 'first'

            elif location == -1:
                newNode.next = self.head
                self.tail.next = newNode
                self.tail = newNode

                location = 'last'

            else:
                currentNode = self.head
                index = 0

                while index < location - 1:
                    currentNode = currentNode.next
                    index += 1

                tempNode = currentNode.next
                currentNode.next = newNode
                newNode.next = tempNode

                if location == 1:
                    location = '1st'
                elif location == 2:
                    location = '2nd'
                elif location == 3:
                    location = '3rd'
                else:
                    location = str(location) + 'th'

            return "Node value ( " + str(nodeValue) + " ) has been successfully inserted at " + str(location) + " location "

    # Traversal of a node in circular singly linked list

    def traverseCSLL(self):
        if self.head is None:
            print("Singly Linked List does not exist")

        else:
            currentNode = self.head
            while currentNode:
                print(currentNode.nodeValue)

                if currentNode.next == self.head:
                    break

                currentNode = currentNode.next

    # # Searching for a node in circular singly linked list
    def searchCSLL(self, searchValue):
        if self.head is None:
            print("Singly Linked List does not exist")

        else:
            currentNode = self.head
            index = 0

            while currentNode:

                if currentNode.nodeValue == searchValue:
                    return "Search value " + str(searchValue) + " is at location " + str(index)
                    # break
                if currentNode.next == self.head:
                    return "Search value " + str(searchValue) + " not found "
                    # break
                currentNode = currentNode.nodeValue
                index += 1

    # Delete  a node from circular singly linked list
    def deleteCSLLNode(self, location):
        if self.head is None:
            print("There is not any node in CSLL")

        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    self.head.next = None

                else:
                    self.head = self.head.next
                    self.tail.next = self.head

            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    self.head.next = None

                else:
                    currentNode = self.head
                    while currentNode:
                        if currentNode.next == self.tail:
                            break
                        currentNode = currentNode.next
                    currentNode.next = self.head
                    self.tail = currentNode

            else:
                currentNode = self.head
                index = 0
                while index < location - 1:
                    currentNode = currentNode.next
                    index += 1

                nextNode = currentNode.next
                currentNode.next = nextNode.next

    # Delete entire circular sinlgy linked list

    def deleteCSLLEntire(self):
        self.head = None
        self.tail.next = None
        self.tail = None


CircularSLL = CircularLinkedList()
# CircularSLL.createSLL(1)

print(CircularSLL.insertCSLL(1, 0))
print(CircularSLL.insertCSLL(3, 0))
print(CircularSLL.insertCSLL(4, 0))

# print([node.nodeValue for node in CircularSLL])

print(CircularSLL.insertCSLL(2, -1))
# CircularSLL.insertCSLL(2, -1)
# print([node.nodeValue for node in CircularSLL])

# CircularSLL.insertCSLL(45, 2)
# CircularSLL.insertCSLL(13, 3)
print(CircularSLL.insertCSLL(45, 2))
print(CircularSLL.insertCSLL(13, 3))
print(CircularSLL.insertCSLL(9, 5))
print([node.nodeValue for node in CircularSLL])

# CircularSLL.traverseCSLL()

# CircularSLL.searchCSLL(2)  # Error in code

CircularSLL.deleteCSLLNode(5)
print([node.nodeValue for node in CircularSLL])

CircularSLL.deleteCSLLEntire()
print([node.nodeValue for node in CircularSLL])
