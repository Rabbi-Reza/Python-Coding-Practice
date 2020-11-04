# Insertion in Singly Linked List

class Node:
    def __init__(self, nodeValue=None):
        self.nodeValue = nodeValue
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Head = Null
        self.tail = None  # Tail = Null

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

    # insert in Linked List
    def insertSinglyLinkedList(self, nodeValue, location):
        newNode = Node(nodeValue)

        # When Linked List is empty
        if self.head is None:
            self.head = newNode
            self.tail = newNode

        else:
            # At first position
            if location == 0:
                newNode.next = self.head
                self.head = newNode

            # At last position
            elif location == -1:
                newNode.next = None
                self.tail.next = newNode  # self.tail represents the last node
                self.tail = newNode

            # At Nth position
            else:
                tempNode = self.head
                index = 0

                while index < location - 1:
                    tempNode = tempNode.next
                    index = index + 1

                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode


SinglyLinkedList = SinglyLinkedList()

SinglyLinkedList.insertSinglyLinkedList(1, -1)
SinglyLinkedList.insertSinglyLinkedList(2, -1)
SinglyLinkedList.insertSinglyLinkedList(3, -1)
SinglyLinkedList.insertSinglyLinkedList(4, -1)

SinglyLinkedList.insertSinglyLinkedList(0, 0)
SinglyLinkedList.insertSinglyLinkedList(10, 1)
SinglyLinkedList.insertSinglyLinkedList(19, 3)
print([node.nodeValue for node in SinglyLinkedList])

# SinglyLinkedList.printSLL()
