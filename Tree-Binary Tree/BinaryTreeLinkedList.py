
import QLL as queue


# =================================================

class Tree:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


newBTree = Tree("Drinks")

left = Tree("Hot")
right = Tree("Cold")

tea = Tree("Tea")
coffee = Tree("Coffee")
left.leftChild = tea
left.rightChild = coffee

soda = Tree("Soda")
fanta = Tree("Fanta")
right.leftChild = soda
right.rightChild = fanta

newBTree.leftChild = left
newBTree.rightChild = right

# =================================================


# Pre-Order Traversal
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
        return "The Binary Tree does not exist"
    else:
        leftLevel = 0
        rightLevel = 0
        customQueue = queue.Queue()
        customQueue.enQueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.deQueue()
            print(root.nodeValue.data)
            if(root.nodeValue.leftChild is not None):
                customQueue.enQueue(root.nodeValue.leftChild)
                leftLevel += 1
            if(root.nodeValue.rightChild is not None):
                customQueue.enQueue(root.nodeValue.rightChild)
                rightLevel += 1
        level = max(leftLevel, rightLevel)
        print("\tLevel of the tree : "+str(level))


# Search in Binary Tree using Level-Order Traversal
def searchBT(rootNode, searchValue):
    if not rootNode:
        return "The BT does not exist"
    else:
        customQueue = queue.Queue()
        customQueue.enQueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.deQueue()
            if root.nodeValue.data == searchValue:
                return "Success !!\n'" + str(searchValue)+"' found in search"
            if (root.nodeValue.leftChild is not None):
                customQueue.enQueue(root.nodeValue.leftChild)
            if (root.nodeValue.rightChild is not None):
                customQueue.enQueue(root.nodeValue.rightChild)
        return "Sorry, '" + str(searchValue) + "' not found in Binart Tree"


# Insert in Binary Tree using Level-Order Traversal
def insertBT(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = queue.Queue()
        customQueue.enQueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.deQueue()
            if root.nodeValue.leftChild is not None:
                customQueue.enQueue(root.nodeValue.leftChild)
            else:
                root.nodeValue.leftChild = newNode
                return "Successfully Inserted to left child"

            if root.nodeValue.rightChild is not None:
                customQueue.enQueue(root.nodeValue.rightChild)
            else:
                root.nodeValue.rightChild = newNode
                return "Successfully Inserted to right child"


# Delete in Binary Tree using Level-Order Traversal
def getDeepestNodeBT(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enQueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.deQueue()
            if(root.nodeValue.leftChild is not None):
                customQueue.enQueue(root.nodeValue.leftChild)
            if(root.nodeValue.rightChild is not None):
                customQueue.enQueue(root.nodeValue.rightChild)
        deepestNode = root.nodeValue
        return deepestNode


def deleteDeepestNodeBT(rootNode, dNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enQueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.deQueue()
            if root.nodeValue is dNode:
                root.nodeValue = None
                return
            if root.nodeValue.rightChild:
                if root.nodeValue.rightChild is dNode:
                    root.nodeValue.rightChild = None
                    return
                else:
                    customQueue.enQueue(root.nodeValue.rightChild)

            if root.nodeValue.leftChild:
                if root.nodeValue.leftChild is dNode:
                    root.nodeValue.leftChild = None
                    return
                else:
                    customQueue.enQueue(root.nodeValue.leftChild)


def deleteNodeBT(rootNode, deleteNode):
    if not rootNode:
        return "The Binary Tree does not exist"
    else:
        customQueue = queue.Queue()
        customQueue.enQueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.deQueue()
            if root.nodeValue.data == deleteNode:
                dNode = getDeepestNodeBT(rootNode)
                root.nodeValue.data = dNode.data
                deleteDeepestNodeBT(rootNode, dNode)
                return "The node has been successfully deleted"
            if(root.nodeValue.leftChild is not None):
                customQueue.enQueue(root.nodeValue.leftChild)
            if(root.nodeValue.rightChild is not None):
                customQueue.enQueue(root.nodeValue.rightChild)
        return "Failed to delete"


# Delete entire Binary Tree
def deleteEntireBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "Entire Binary Tree is successfully deleted"


print('-------------', end="\n\n")

print('------Pre-Order Traversal-------')
preOrderTraversal(newBTree)

print('------In-Order Traversal-------')
inOrderTraversal(newBTree)

print('------Post-Order Traversal-------')
postOrderTraversal(newBTree)

print('------Level-Order Traversal-------')
levelOrderTraversal(newBTree)

print('-------Search------')
# seachValue = input("Enter search value : ")
searchValue = "Soda"
print(searchBT(newBTree, searchValue))

print('-------Insert------')
# searchValue = input("Enter search value : ")
newNode = Tree("Lemon Tea")
print(insertBT(newBTree, newNode))
levelOrderTraversal(newBTree)

print('-------Delete Node------')
# deepestNode = getDeepestNodeBT(newBTree)
# deleteDeepestNodeBT(newBTree, deepestNode)
# # print(deepestNode.data)
# levelOrderTraversal(newBTree)
# print(deepestNode.data)

# deleteNodeBT(newBTree, "Tea")
# levelOrderTraversal(newBTree)

print('-------Delete Entire BT------')
deleteEntireBT(newBTree)
levelOrderTraversal(newBTree)
