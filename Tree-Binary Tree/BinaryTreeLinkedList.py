
# import QueueLinkedListBT as queue


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


# # Level-Order Traversal
# def levelOrderTraversal(rootNode):
#     if not rootNode:
#         return
#     else:
#         customQueue = queue.Queue()
#         customQueue.enqueue(rootNode)
#         while not(customQueue.isEmpty()):
#             root = customQueue.dequeue()
#             print(root.value.data)
#             if(root.value.leftChild is not None):
#                 customQueue.enqueue(root.value.leftChild)
#             if(root.value.rightChild is not None):
#                 customQueue.enqueue(root.value.rightChild)


print('-------------')

preOrderTraversal(newBTree)
print('-------------')

inOrderTraversal(newBTree)
print('-------------')

postOrderTraversal(newBTree)
print('-------------')

# levelOrderTraversal(newBTree)
print('-------------')
