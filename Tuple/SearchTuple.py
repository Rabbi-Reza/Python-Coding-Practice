#  How to search for an element in Tuple

myTuple = ('a', 'b', 'c', 'd', 'e')

print('a' in myTuple)
print('x' in myTuple)

print('--------')

def searchTupleByValue(mTuple,element):
    for i in mTuple:
        if i == element:
            return mTuple.index(i)
    return 'Element does not exist'

def searchTupleByIndex(mTuple,index):
    for i in range(len(mTuple)):
        if i == index:
            return mTuple[i]
    return 'Index does not exist'

print(searchTupleByValue(myTuple,'b'))
print(searchTupleByValue(myTuple,'x'))

print(searchTupleByIndex(myTuple,2))
print(searchTupleByIndex(myTuple,7))