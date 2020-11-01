
import numpy as np

twoDArray = np.array([ [11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9] ])

print(twoDArray)

# Insert in an 2D array
print("Insert an array")
newTwoDArray = np.insert(twoDArray, 1, [[1,2,3,4]], axis=0) #row
print(newTwoDArray)

newTwoDArray = np.insert(twoDArray, 4, [[1,2,3,4]], axis=1) #column
print(newTwoDArray)

print(len(twoDArray))

newTwoDArray = np.append(twoDArray, [[1,2,3,4]], axis=0) #row
print(newTwoDArray)

newTwoDArray = np.append(twoDArray, [[1],[2],[3],[4]], axis=1) #column
print(newTwoDArray)

print(len(newTwoDArray[0]))

# Accessing an element from an 2D array
def access2DArray(array,rowIndex,colIndex):
    if rowIndex >= len(array) or colIndex >= len(array):
        print("Incorrect index")
    else:
        print(array[rowIndex][colIndex])

access2DArray(newTwoDArray,2,6)

# Traverse an 2D array
def traverseTDArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

def traverse2DArray(array):
    for row in range(len(array)):
        for col in range(len(array)):

            print(array[row][col])

traverseTDArray(twoDArray)
traverse2DArray(twoDArray)

# Search in an 2D array
def searchIn2DArray(array,value):
    for row in range(len(array)):
        for col in range(len(array)):
            if array[row][col] == value:
                # print( value , "is at loction" , row , col)
                return str(value) + " is at loction => " + str(row) + " " + str(col)
    return "Element not found"

print(searchIn2DArray(twoDArray,11))
print(searchIn2DArray(twoDArray,60))

# Delete in an 2D array
newDeleted2DArray = np.delete(twoDArray,1,axis=0)
print(newDeleted2DArray)