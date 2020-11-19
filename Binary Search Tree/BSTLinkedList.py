import QLL as queue


# Creation of BST
class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


# Insert a node in BST
def insertNodeBST(rootNode, insertValue):
    if rootNode.data == None:
        rootNode.data = insertValue
    # Insert in left child (if value is less then root)
    elif insertValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(insertValue)
        else:
            insertNodeBST(rootNode.leftChild, insertValue)
    # Insert in right child (if value is larger then root)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(insertValue)
        else:
            insertNodeBST(rootNode.rightChild, insertValue)
    return "The node has been successfully inserted"


# Pre-Order Traversal (root -> left -> right)
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


# In-Order Traversal
def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)


# Post-Order Traversal
def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)


# Level-Order Traversal
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        leftLevel = 0
        rightLevel = 0
        customQueue = queue.Queue()
        customQueue.enQueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.deQueue()
            print(root.nodeValue.data)
            if root.nodeValue.leftChild is not None:
                customQueue.enQueue(root.nodeValue.leftChild)
                leftLevel += 1
            if root.nodeValue.rightChild is not None:
                customQueue.enQueue(root.nodeValue.rightChild)
                rightLevel += 1
        level = max(leftLevel, rightLevel)
        print("Level : " + str(level))


# Search in Binary Tree
def searchNodeBST(rootNode, searchValue):
    if rootNode.data == searchValue:
        print("The value " + str(searchValue) + " is found")
    elif searchValue < rootNode.data:
        if rootNode.leftChild.data == searchValue:
            print("The value " + str(searchValue) + " is found")
        else:
            searchNodeBST(rootNode.leftChild, searchValue)
    else:
        if rootNode.rightChild.data == searchValue:
            print("The value " + str(searchValue) + " is found")
        else:
            searchNodeBST(rootNode.rightChild, searchValue)


# Delete a node in Binary Tree
def minValueNodeBST(bstNode):
    current = bstNode
    while (current.leftChild is not None):
        current = current.leftChild
    return current


def deleteNodeBST(rootNode, deleteValue):
    if rootNode is None:
        return rootNode
    if deleteValue < rootNode.data:
        rootNode.leftChild = deleteNodeBST(rootNode.leftChild, deleteValue)
    elif deleteValue > rootNode.data:
        rootNode.rightChild = deleteNodeBST(rootNode.rightChild, deleteValue)

    # Delete a node with one child or zero child
    else:
        if rootNode.leftChild is None:
            tempNode = rootNode.rightChild
            rootNode = None
            return tempNode
        if rootNode.rightChild is None:
            tempNode = rootNode.leftChild
            rootNode = None
            return tempNode

    # Delete a node with two child
        tempNode = minValueNodeBST(rootNode.rightChild)
        rootNode.data = tempNode.data
        rootNode.rightChild = deleteNodeBST(rootNode.rightChild, tempNode.data)
    return rootNode


# Delete a node in Binary Tree
def deleteEntireBST(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "Entire BST has been successfully deleted"


newBST = BSTNode(None)
print(insertNodeBST(newBST, 70))
print(insertNodeBST(newBST, 50))
print(insertNodeBST(newBST, 90))
print(insertNodeBST(newBST, 30))
print(insertNodeBST(newBST, 60))
print(insertNodeBST(newBST, 80))
print(insertNodeBST(newBST, 100))
print(insertNodeBST(newBST, 20))
print(insertNodeBST(newBST, 40))


# print(newBST.data)
# print(newBST.leftChild.data)
# print(newBST.rightChild.data)

print('------Pre-Order Traversal-------')
preOrderTraversal(newBST)

print('------In-Order Traversal-------')
inOrderTraversal(newBST)

print('------Post-Order Traversal-------')
postOrderTraversal(newBST)

print('------level-Order Traversal-------')
levelOrderTraversal(newBST)

print('------Search a node in BST-------')
searchNodeBST(newBST, 60)

print('------Delete a node in BST-------')
print(deleteNodeBST(newBST, 20))

print('------level-Order Traversal-------')
levelOrderTraversal(newBST)

print('------Delete entire BST-------')
print(deleteEntireBST(newBST))
