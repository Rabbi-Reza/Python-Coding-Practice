# Creation of Singly Linked List

class Node:
    def __init__(self, nodeValue=None):
        self.nodeValue = nodeValue
        self.nextNode = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Head = Null
        self.tail = None  # Tail = Null


SinglyLinkedList = SinglyLinkedList()
node1 = Node(2)
node2 = Node(5)

SinglyLinkedList.head = node1
SinglyLinkedList.head.nextNode = node2
SinglyLinkedList.tail = node2
