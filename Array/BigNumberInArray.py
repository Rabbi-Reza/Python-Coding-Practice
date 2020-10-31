
def findBiggestNumber(sampleArray):
    biggestNumber = sampleArray[0]

    for index in range(1,len(sampleArray)):
        if sampleArray[index] > biggestNumber:
            biggestNumber = sampleArray[index]

    return biggestNumber


# Recursive algorithm
def findMaxNumRec(sampleArray, n):
    if n == 1:
       return sampleArray[0]

    return max(sampleArray[n-1],findMaxNumRec(sampleArray,n-1))


sample1Array = [1,10,45,33,23,45,67,2,3,33,55,11,65,76,34,35,27,99]

print(findBiggestNumber(sample1Array))
print(findMaxNumRec(sample1Array,len(sample1Array)))