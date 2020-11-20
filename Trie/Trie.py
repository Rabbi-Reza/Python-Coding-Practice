# Creation
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert a string in trie
    def insertString(self, insertWord):
        current = self.root
        for i in insertWord:
            ch = i
            newNode = current.children.get(ch)
            if newNode == None:
                newNode = TrieNode()
                current.children.update({ch: newNode})
            current = newNode
        current.endOfString = True
        print("Successfully inserted")

    # Search a string in trie
    def searchString(self, searchWord):
        currentNode = self.root

        for i in searchWord:
            newNode = currentNode.children.get(i)
            # Not matched String
            if newNode == None:
                return False
            currentNode = newNode

        # Fully matched String
        if currentNode.endOfString == True:
            return True
        # Part of String Matched
        else:
            return False


# Delete a string in trie
def deleteString(root, deleteWord, index):
    ch = deleteWord[index]
    currentNode = root.children.get(ch)
    canThisNodeBeDeleted = False

    if len(currentNode.children) > 1:
        deleteString(currentNode, deleteWord, index + 1)
        return False

    if index == len(deleteWord) - 1:
        if len(currentNode.children) >= 1:
            currentNode.endOfString = False
            return False
        else:
            root.children.pop(ch)
            return True

    if currentNode.endOfString == True:
        deleteString(currentNode, deleteWord, index + 1)
        return False

    canThisNodeBeDeleted = deleteString(currentNode, deleteWord, index + 1)
    if canThisNodeBeDeleted == True:
        root.children.pop(ch)
        return True
    else:
        return False


print("-------- Creation ---------")
newTrie = Trie()

print("-------- Insert a String---------")
newTrie.insertString("App")
newTrie.insertString("AppL")

print("-------- Search a String ---------")
print(newTrie.searchString("App"))
print(newTrie.searchString("Ap"))
print(newTrie.searchString("Bar"))

print("-------- Delete a String ---------")
print(deleteString(newTrie.root, "App", 0))
print(newTrie.searchString("App"))
