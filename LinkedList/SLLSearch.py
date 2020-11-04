

class Node:
    def __init__(self, nodeValue=None):
        self.nodeValue = nodeValue
        self.next = None


class SLLTraverse:
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

# Insertion in Singly Linked List

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
                tempNode = self.head
                index = 0

                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1

                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

# Traverse Singly Linked List
    def traverseSLL(self):
        if self.head is None:
            print("Singly Linked List does not exist")
        else:
            temp = self.head
            while temp is not None:
                print(temp.nodeValue)
                temp = temp.next

# Search for a node in Singly Linked List
    def searchSLL(self, searchValue):

        if self.head is None:
            return "Singly Linked List does not exist"

        else:
            temp = self.head
            index = -1
            while temp is not None:
                index += 1
                if temp.nodeValue == searchValue:
                    return str(temp.nodeValue) + ' at location ' + str(index)
                temp = temp.next

            return "Search value does not exist in the Linked List"


SLLTraverse = SLLTraverse()

SLLTraverse.insertSLL(1, -1)
SLLTraverse.insertSLL(2, -1)
SLLTraverse.insertSLL(3, -1)
SLLTraverse.insertSLL(4, -1)

SLLTraverse.insertSLL(0, 0)
SLLTraverse.insertSLL(10, 1)
SLLTraverse.insertSLL(19, 3)
print([node.nodeValue for node in SLLTraverse])

print(SLLTraverse.searchSLL(1))
