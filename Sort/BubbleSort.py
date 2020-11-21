
# from array import *


# def bubbleSort(arr, n):
#     for i in range(n-1):
#         for j in range(n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]


# arr = array('i', [])

# n = int(input("Enter array size : "))
# for i in range(n):

#     arrVal = int(input("Enter " + str(i+1)+" element : "))
#     arr.append(arrVal)

# print(" Array is : ", arr)

# bubbleSort(arr, n)
# print("Sorted array is : ", arr)

# Bubble sort
def bubbleSort2(customList):
    for i in range(len(customList) - 1):
        for j in range(len(customList) - i - 1):
            if customList[j] > customList[j+1]:
                customList[j], customList[j+1] = customList[j+1], customList[j]
    print(customList)


cList = [2, 1, 7, 6, 5, 3, 4, 9, 8]
bubbleSort2(cList)
