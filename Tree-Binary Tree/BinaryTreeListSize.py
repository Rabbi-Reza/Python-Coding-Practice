
class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    # Insert a Node in Binary Tree
    def insertNode(self, insertValue):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "The Binary Tree is full"
        self.customList[self.lastUsedIndex + 1] = insertValue
        self.lastUsedIndex += 1
        return "The value has been succesfully inserted"

    # Search in Binary Tree
    def searchNodeBT(self, searchValue):
        for i in range(len(self.customList)):
            if self.customList[i] == searchValue:
                return "Success !!\n'" + str(searchValue)+"' found in Binary Tree"
        return "Sorry, '" + str(searchValue) + "' not found in Binart Tree"

    # Pre-Order Traversal (root -> left -> right)
    def preOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index * 2)
        self.preOrderTraversal(index * 2 + 1)

    # In-Order Traversal ( left -> root -> right)
    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index * 2)
        print(self.customList[index])
        self.inOrderTraversal(index * 2 + 1)

    # Post-Order Traversal (root -> right -> left )
    def postOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(index * 2)
        self.postOrderTraversal(index * 2 + 1)
        print(self.customList[index])

    # Level-Order Traversal (nodeOfLevel 1 left to right -> nodeOfLevel 2 left to right -> nodeOfLevel 3 left to right)
    def levelOrderTraversal(self, index):
        for i in range(index, self.lastUsedIndex + 1):
            print(self.customList[i])

    # Delete a node in Binary Tree
    def deleteNodeBT(self, deleteValue):
        if self.lastUsedIndex == 0:
            return "There is not any node to delete"
        for i in range(1, self.lastUsedIndex + 1):
            if self.customList[i] == deleteValue:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "The node '" + str(deleteValue) + "' has been successfuly deleted"
        return str(deleteValue) + " not found to delete"

    # Delete entire Binary Tree
    def deleteEntireBT(self):
        self.customList = None
        return "The Binary Tree has been successfully deleted"


newBT = BinaryTree(8)

print(newBT.insertNode("Drinks"))
print(newBT.insertNode("Hot"))
print(newBT.insertNode("Cold"))
print(newBT.insertNode("Tea"))
print(newBT.insertNode("Coffee"))

print('------Search a node in BT-------')
print(newBT.searchNodeBT("Fanta"))
print(newBT.searchNodeBT("Hot"))

print('------Pre-Order Traversal-------')
newBT.preOrderTraversal(1)

print('------In-Order Traversal-------')
newBT.inOrderTraversal(1)

print('------Post-Order Traversal-------')
newBT.postOrderTraversal(1)

print('------level-Order Traversal-------')
newBT.levelOrderTraversal(1)

print('------Delete a node in BT-------')
print(newBT.deleteNodeBT("Tea"))
newBT.levelOrderTraversal(1)

print('------Delete entire BT-------')
print(newBT.deleteEntireBT())
# newBT.levelOrderTraversal(1)
