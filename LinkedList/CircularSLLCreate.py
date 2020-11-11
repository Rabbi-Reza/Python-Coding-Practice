#   Create Circular Linked List
class Node:
    def __init__(self, nodeValue=None):
        self.nodeValue = nodeValue
        self.next = None


class CircularLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        tempNode = self.head
        while tempNode:
            yield tempNode
            if tempNode.next == self.head:
                break
            tempNode = tempNode.next

    #  Creation of circular singly linked list
    def createSLL(self, nodeValue):
        node = Node(nodeValue)

        node.next = node
        self.head = node
        self.tail = node

        return 'Circular Singly Linked List Created'


CircularSLL = CircularLinkedList()
CircularSLL.createSLL(1)

print([node.nodeValue for node in CircularSLL])
