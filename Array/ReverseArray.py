
# from array import *
#
# def reverseArray(array):
#     array1 = array
#
#     if len(array) == 0:
#         return array1
#     else:
#         array1[0] = array[-1]
#         return reverseArray(array[1:-1])

def reverse(array):

    for i in range(0,int(len(array)/2)):
        other = len(array)-i-1
        temp = array[i]
        array[i] = array[other]
        array[other] = temp

    return array

# Reversing a list using reverse()
def ReverseFunc(lst):
    lst.reverse()
    return lst

arrayA = [1,8,3,5,2]

# print(len(arrayA))

print(reverse(arrayA))
#
# print(reverseArray(arrayA))

# print(ReverseFunc(arrayA))