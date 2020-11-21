
# # Linear Search
# from array import *


def linearSearch(arr, n, value):
    for i in range(0, n):
        if(arr[i] == value):
            return i+1

    return -1


# arr = array('i', [])


# num = int(input("Enter size of array:"))

# for i in range(1, num+1):
#     arrVal = int(input(" Enter " + str(i)+" item: "))
#     arr.append(arrVal)


# print("Input array is: ", arr)

# value = int(input("Enter search value:"))


# result = linearSearch(arr, num, value)

# if(result == -1):
#     print("Search value is not in array !!")
# else:
#     print("Search value ", value, " is on location ", result)

def linearSearch2(array, searchValue):
    for index in range(len(array)):
        if array[index] == searchValue:
            return index
    return -1


arrayList = [20, 40, 10, 30, 50, 90]
print(linearSearch2(arrayList, 50))
print(linearSearch2(arrayList, 100))
