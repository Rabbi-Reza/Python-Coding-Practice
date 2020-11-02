import numpy as np

# 1
A = np.array([0, 2, 4, 6, 4, 1, 5, 3])
a = [0, 2, 4, 6, 4, 1, 5, 3]

A = A.sort()
print(A)
a = a.sort()
print(a)

# 2
myArray = np.array([1, 2, 3, 4, 5, 6])
myList = [1, 2, 3, 4, 5, 6]

print(myArray/2)
# Error
# print(myList/2)

# 3
myArray = np.array([1, 2, 3, 4, 5, 6, 'a'])
myList = [1, 2, 3, 4, 5, 6, 'a']

print(myArray)
print(myList)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[::2])
