import math
# from array import *


def binarySearchRecursion(array, first, last, value):
    if last >= first:
        mid = first + (last - first) // 2

    if array[mid] == value:
        return mid
    elif array[mid] > value:
        return binarySearchRecursion(array, first, mid - 1, value)
    else:
        return binarySearchRecursion(array, mid+1, last, value)

    return -1


# arr = array('i',[])

# num = int(input("Enter Array size : "))

# for i in range(0,num):
#     arrValue = int(input(" Enter Sorted array value of element " + str(i+1) + " : "))
#     arr.append(arrValue)

# print(" Sorted array elements are : ", arr)

# value = int(input("Enter search value : "))

# result = binarySearchRecursion(arr, 0, num - 1, value)

# if result == -1:
#     print(" Value not found !! ")
# else:
#     print(" Value ", value, " is on location : ", result)


def binarySearch(array, searchValue):
    start = 0
    end = len(array) - 1
    middle = math.floor((start + end) / 2)

    while not(array[middle] == searchValue) and start <= end:
        #  Moving left side of middle value, so end shift to left
        if searchValue < array[middle]:
            end = middle - 1
        #  Moving right side of middle value, so start shift to right
        else:
            start = middle + 1
        middle = math.floor((start + end) / 2)
    if array[middle] == searchValue:
        return middle
    else:
        return -1


arrayList = [8, 9, 12, 15, 17, 19, 20, 21, 28]
print(binarySearch(arrayList, 15))
print(binarySearch(arrayList, 18))
