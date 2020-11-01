
from array import *

arr1 = array('i',[1,2,3,4,5,6])
arr2 = array('d',[1.1,1.2,1.3,4])

print(arr1)

# Insert an element in array
arr1.insert(0,0)
arr1.insert(6,9)
print(arr1)

# Traverse an array
def traverseArray(array):
    for i in array:
        print(i)

traverseArray(arr1)

# Accessing an array element
def accessArray(array,index):
    if index >= len(array):
        print("Index is out of array size")
    else:
        print(array[index])

accessArray(arr1,4)

# Search an array element
def searchInArrayLinear(array,value):
    for i in array:
        if i == value:
            return array.index(value)

    return "Value is not in the array"

print(searchInArrayLinear(arr1,9))

# Delete an array element
def deleteArray(array,value):
    for i in array:
        if i == value:
            array.remove(value)
            return array

    return "Value is not in the array"

print(deleteArray(arr1,9))

