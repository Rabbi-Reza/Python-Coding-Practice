
# Tuple Operations
myTuple = (1,4,3,2,5)
myTuple1 = (1,2,6,9,8,7,2)

print(myTuple + myTuple1)
print(myTuple * 4)
print(2 in myTuple1)
print(4 in myTuple1)

# Tuple Methods
print(myTuple1.count(2))
print(myTuple1.index(2))

# Tuple Built in Functions
print(len(myTuple1))

print(max(myTuple1))
print(min(myTuple1))

myList = [1,3,4,2,7,5,9]
print(tuple(myList))
ListToTuple = tuple(myList)
print(ListToTuple)