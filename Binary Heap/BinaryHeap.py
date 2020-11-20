# Implementation option:
#     1. Array Implementation (*)
#     2. Reference/ Pointer Implementation

# Creation
class Heap:
    def __init__(self, size):
        self.customList = (size + 1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1


# Peek of Heap
def peekOfHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.customList[1]


# Size of Heap
def sizeOfHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapSize


# Level Order Traversal
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1, rootNode.heapSize + 1):
            print(rootNode.customList[i])


# Insertion
def heapifyTreeInsert(rootNode, index, heapType):
    parentIndex = int(index/2)
    if index <= 1:
        return
    if heapType == "Min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            # Swap
            # currentNode = rootNode.customList[index]
            # rootNode.customList[index] = rootNode.customList[parentIndex]
            # rootNode.customList[parentIndex] = currentNode

            # Swap (python)
            rootNode.customList[index], rootNode.customList[parentIndex] = rootNode.customList[parentIndex], rootNode.customList[index]

        heapifyTreeInsert(rootNode, parentIndex, heapType)

    elif heapType == "Max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            # Swap
            # currentNode = rootNode.customList[index]
            # rootNode.customList[index] = rootNode.customList[parentIndex]
            # rootNode.customList[parentIndex] = currentNode

            # Swap (python)
            rootNode.customList[index], rootNode.customList[parentIndex] = rootNode.customList[parentIndex], rootNode.customList[index]

        heapifyTreeInsert(rootNode, parentIndex, heapType)


def insertNodeBH(rootNode, insertValue, heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "The Binary Heap is full"
    rootNode.customList[rootNode.heapSize + 1] = insertValue
    rootNode.heapSize += 1
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
    return "The value " + str(insertValue) + " has been successfully inserted"


# Extract
def heapifyTreeExtract(rootNode, index, heapType):
    leftIndex = index * 2
    rightIndex = index * 2 + 1
    swapChild = 0

    # No Child
    if rootNode.heapSize < leftIndex:
        return
    # One Child
    elif rootNode.heapSize == leftIndex:
        if heapType == "Min":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                # Swap
                currentNode = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = currentNode
            return
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                # Swap
                currentNode = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = currentNode
            return
    # Both Child
    else:
        # Smaller
        if heapType == "Min":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                currentNode = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = currentNode
        # Biggar
        else:
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                currentNode = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = currentNode

        heapifyTreeExtract(rootNode, swapChild, heapType)


def extractNode(rootNode, heapType):
    if rootNode.heapSize == 0:
        return
    else:
        extractedNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -= 1
        heapifyTreeExtract(rootNode, 1, heapType)
        return extractedNode


# Delete Entire Binary Heap
def deleteEntireBH(rootNode):
    rootNode.customList = None
    return "Entire Binary Heap is deleted"


print("----------- Creation ------------")
newBinaryHeap = Heap(5)

print("----------- Insert a node in Binary Heap ------------")
print(insertNodeBH(newBinaryHeap, 4, "Max"))
print(insertNodeBH(newBinaryHeap, 5, "Max"))
print(insertNodeBH(newBinaryHeap, 2, "Max"))
print(insertNodeBH(newBinaryHeap, 1, "Max"))

print("----------- Size of Heap ------------")
print(sizeOfHeap(newBinaryHeap))

print("----------- Level order traversal ------------")
levelOrderTraversal(newBinaryHeap)

print("----------- Extract ------------")
print(extractNode(newBinaryHeap, "Max"))

print("----------- Level order traversal ------------")
levelOrderTraversal(newBinaryHeap)

print("----------- Delete Entire Binary Heap ------------")
print(deleteEntireBH(newBinaryHeap))

# print("----------- Level order traversal ------------")
# levelOrderTraversal(newBinaryHeap)
