
from array import *

def binarySearch(arr, first, last, value):
    if last >= first:
        mid = first + (last - first) // 2

    if arr[mid] == value:
        return mid
    elif arr[mid] > value:
        return binarySearch(arr, first, mid - 1, value)
    else:
        return binarySearch(arr,mid+1,last,value)

    return -1



arr = array('i',[])

num = int(input("Enter Array size : "))

for i in range(0,num):
    arrValue = int(input(" Enter Sorted array value of element " + str(i+1) + " : "))
    arr.append(arrValue)

print(" Sorted array elements are : ", arr)

value = int(input("Enter search value : "))

result = binarySearch(arr, 0, num - 1, value)

if result == -1:
    print(" Value not found !! ")
else:
    print(" Value ", value, " is on location : ", result)
