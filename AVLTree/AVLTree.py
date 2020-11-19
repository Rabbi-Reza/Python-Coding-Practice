import QLL as queue


class AVLNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1


def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)


def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enQueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.deQueue()
            print(root.nodeValue.data)
            if root.nodeValue.leftChild is not None:
                customQueue.enQueue(root.nodeValue.leftChild)
            if root.nodeValue.rightChild is not None:
                customQueue.enQueue(root.nodeValue.rightChild)


# Search in AVL Tree
def searchNodeAVL(rootNode, searchValue):
    if rootNode.data == searchValue:
        print("The value " + str(searchValue) + " is found")

    elif searchValue < rootNode.data:
        if rootNode.leftChild.data == searchValue:
            print("The value " + str(searchValue) + " is found")
        else:
            searchNodeAVL(rootNode.leftChild, searchValue)

    else:
        if rootNode.rightChild.data == searchValue:
            print("The value " + str(searchValue) + " is found")
        else:
            searchNodeAVL(rootNode.rightChild, searchValue)


# Insertion in AVL Tree
def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height


def rightRotate(disbalanceNode):
    newRoot = disbalanceNode.leftChild
    disbalanceNode.leftChild = disbalanceNode.leftChild.rightChild
    newRoot.rightChild = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftChild),
                                    getHeight(disbalanceNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild),
                             getHeight(newRoot.rightChild))
    return newRoot


def leftRotate(disbalanceNode):
    newRoot = disbalanceNode.rightChild
    disbalanceNode.rightChild = disbalanceNode.rightChild.leftChild
    newRoot.leftChild = disbalanceNode
    disbalanceNode.height = 1 + \
        max(getHeight(disbalanceNode.leftChild),
            getHeight(disbalanceNode.rightChild))
    newRoot.height = 1 + \
        max(getHeight(newRoot.leftChild),
            getHeight(newRoot.rightChild))
    return newRoot


def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)


def insertNodeAVL(rootNode, insertValue):
    if not rootNode:
        return AVLNode(insertValue)
    elif insertValue < rootNode.data:
        rootNode.leftChild = insertNodeAVL(rootNode.leftChild, insertValue)
    else:
        rootNode.rightChild = insertNodeAVL(rootNode.rightChild, insertValue)
    rootNode.height = 1 + \
        max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)

    # left-left
    if balance > 1 and insertValue < rootNode.leftChild.data:
        return rightRotate(rootNode)

    # left-right
    if balance > 1 and insertValue > rootNode.leftChild.data:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)

    # right-right
    if balance < -1 and insertValue > rootNode.rightChild.data:
        return leftRotate(rootNode)

    # right-left
    if balance < -1 and insertValue < rootNode.rightChild.data:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)

    return rootNode


# Delete a node in AVL Tree
def getMinValueNode(rootNode):
    if rootNode is None or rootNode.leftChild is None:
        return rootNode
    return getMinValueNode(rootNode.leftChild)


def deleteNodeAVL(rootNode, deleteValue):
    if not rootNode:
        return rootNode

    elif deleteValue < rootNode.data:
        rootNode.leftChild = deleteNodeAVL(rootNode.leftChild, deleteValue)
    elif deleteValue > rootNode.data:
        rootNode.rightChild = deleteNodeAVL(rootNode.rightChild, deleteValue)

    else:
        if rootNode.leftChild is None:
            tempNode = rootNode.rightChild
            rootNode = None
            return tempNode
        elif rootNode.rightChild is None:
            tempNode = rootNode.leftChild
            rootNode = None
            return tempNode
        tempNode = getMinValueNode(rootNode.rightChild)
        rootNode.data = tempNode.data
        rootNode.rightChild = deleteNodeAVL(rootNode.rightChild, tempNode.data)

    # Rotation is required
    balance = getBalance(rootNode)
    # left - left
    if balance > 1 and getBalance(rootNode.leftChild) >= 0:
        return rightRotate(rootNode)
    # right - right
    if balance < -1 and getBalance(rootNode.rightChild) <= 0:
        return leftRotate(rootNode)
    # left - right
    if balance > 1 and getBalance(rootNode.leftChild) < 0:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    # right - left
    if balance < -1 and getBalance(rootNode.rightChild) > 0:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)

    return rootNode


# Delete a node in AVL Tree
def deleteEntireAVL(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "Entire AVL has been successfully deleted"


print("-------Create AVL---------")
newAVL = AVLNode(5)

print("-------Insert a Node in AVL---------")
newAVL = insertNodeAVL(newAVL, 10)
newAVL = insertNodeAVL(newAVL, 15)
newAVL = insertNodeAVL(newAVL, 20)

print("-------Delete a Node in AVL---------")
deleteNodeAVL(newAVL, 15)
levelOrderTraversal(newAVL)

print("-------Delete Entire AVL---------")
print(deleteEntireAVL(newAVL))
levelOrderTraversal(newAVL)
