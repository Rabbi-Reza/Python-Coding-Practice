class Node:
    def __init__(self, nodeValue=None):
        self.nodeValue = nodeValue
        self.next = None


class SLLDeletion:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def printSLL(self):
        temp = self.head
        while temp:
            print(temp.nodeValue)
            temp = temp.next

# Insert in Singly Linked List
    def insertSLL(self, nodeValue, location):
        newNode = Node(nodeValue)

        if self.head is None:
            self.head = newNode
            self.tail = newNode

        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode

            elif location == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode

            else:
                currentNode = self.head
                index = 0

                while index < location - 1:
                    currentNode = currentNode.next
                    index += 1

                tempNode = currentNode.next
                currentNode.next = newNode
                newNode.next = tempNode

# Traverse Singly Linked List
    def traverseSLL(self):

        if self.head is None:
            print("Singly Linked List does not exist")
        else:
            currentNode = self.head
            while currentNode is not None:
                print(currentNode.nodeValue)
                currentNode = currentNode.next

# Search for a node in Singly Linked List
    def searchSLL(self, searchValue):

        if self.head is None:
            return "Singly Linked List does not exist"

        else:
            currentNode = self.head
            index = -1
            while currentNode is not None:
                index += 1
                if currentNode.nodeValue == searchValue:
                    return str(currentNode.nodeValue) + ' at location ' + str(index)
                currentNode = currentNode.next

            return "Search value does not exist in the Linked List"


#  Delete a node from Singly Linked List

    def SLLDeleteNode(self, location):

        if self.head is None:
            print("Singly Linked List does not exist")

        else:

            # If want to delete from 1st position
            if location == 0:

                # If only one node
                if self.head == self.tail:
                    self.head = None
                    self.tail = None

                # If more then one node in List
                else:
                    self.head = self.head.next

            # If want to delete from last position
            elif location == -1:

                # If only one node
                if self.head == self.tail:
                    self.head = None
                    self.tail = None

                # If more then one node in List
                else:
                    currentNode = self.head

                    while currentNode is not None:
                        if currentNode.next == self.tail:
                            break
                        currentNode = currentNode.next

                    currentNode.next = None
                    self.tail = currentNode

            # If want to delete from Nth position
            else:
                currentNode = self.head
                index = 0

                while index < location - 1:
                    currentNode = currentNode.next
                    index += 1

                nextNode = currentNode.next
                currentNode.next = nextNode.next

#  Delete entire Singly Linked List
    def SLLDeleteEntireList(self):
        if self.head is None:
            print("Singly Linked List does not exist")

        else:
            self.head = None
            self.tail = None


SLLDelete = SLLDeletion()

SLLDelete.insertSLL(1, -1)
SLLDelete.insertSLL(2, -1)
SLLDelete.insertSLL(3, -1)
SLLDelete.insertSLL(4, -1)
SLLDelete.insertSLL(0, 0)
SLLDelete.insertSLL(10, 1)
SLLDelete.insertSLL(19, 3)
print([node.nodeValue for node in SLLDelete])

SLLDelete.SLLDeleteNode(1)
print([node.nodeValue for node in SLLDelete])

SLLDelete.SLLDeleteEntireList()
print([node.nodeValue for node in SLLDelete])
SLLDelete.SLLDeleteEntireList()
print([node.nodeValue for node in SLLDelete])
