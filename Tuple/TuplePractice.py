
#  How to create a Tuple
newTuple = ('a', 'b', 'c', 'd', 'e')
print(newTuple)

newTuple2 = ('a',)
print(newTuple2)

newTuple2 = ('a')
print(newTuple2)

newTuple1 = tuple()
print(newTuple1)

newTuple1 = tuple('abcde')
print(newTuple1)

#  How to access a Tuple
myTuple = ('a', 'b', 'c', 'd', 'e')
print(myTuple[2])
print(myTuple[-1])

print(myTuple[1:3])
print(myTuple[:3])
print(myTuple[2:])
print(myTuple[:])

#  Reassign a Tuple
tuple1 = 0,1,2,3,4,5,6
print(tuple1)
tuple1 = 0,1,2,3,4,5,6
print(tuple1)

tuple1 = 7,8,9,0
print(tuple1)

#  Delete a Tuple
tuple1 = 0,1,2,3,4,5,6
del tuple1
# Tuple is deleted so print will show error
# print(tuple1)

# Tuples can be stored in List
List2 = [(1,2),(5,7)]
print(List2)
List2 = [[1,2],[5,7]]
print(List2)

# Lists can be stored in Tuple
tuple2 = ([1,2],[5,7])
print(tuple2)
tuple2 = ((1,2),(5,7))
print(tuple2)