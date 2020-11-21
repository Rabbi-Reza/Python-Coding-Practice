
def merge(customList, leftIndex, middleIndex, rightIndex):
    numberOfElementsFirstSubArray = middleIndex - leftIndex + 1
    numberOfElementsSecondSubArray = rightIndex - middleIndex
    # Divided the array in two sub-array
    leftArray = [0] * numberOfElementsFirstSubArray
    rightArray = [0] * numberOfElementsSecondSubArray

    for indexOfLeftSubArray in range(0, numberOfElementsFirstSubArray):
        leftArray[indexOfLeftSubArray] = customList[leftIndex +
                                                    indexOfLeftSubArray]

    for indexOfRightSubArray in range(0, numberOfElementsSecondSubArray):
        rightArray[indexOfRightSubArray] = customList[middleIndex +
                                                      1 + indexOfRightSubArray]

    indexOfLeftSubArray = 0
    indexOfRightSubArray = 0
    indexOfMergeSubArray = leftIndex
    # Coping items in array for merging
    while indexOfLeftSubArray < numberOfElementsFirstSubArray and indexOfRightSubArray < numberOfElementsSecondSubArray:
        if leftArray[indexOfLeftSubArray] <= rightArray[indexOfRightSubArray]:
            customList[indexOfMergeSubArray] = leftArray[indexOfLeftSubArray]
            indexOfLeftSubArray += 1
        else:
            customList[indexOfMergeSubArray] = rightArray[indexOfRightSubArray]
            indexOfRightSubArray += 1
        indexOfMergeSubArray += 1
    # Coping left Array Elements if any remaining
    while indexOfLeftSubArray < numberOfElementsFirstSubArray:
        customList[indexOfMergeSubArray] = leftArray[indexOfLeftSubArray]
        indexOfLeftSubArray += 1
        indexOfMergeSubArray += 1
    # Coping right Array Elements if any remaining
    while indexOfRightSubArray < numberOfElementsSecondSubArray:
        customList[indexOfMergeSubArray] = rightArray[indexOfRightSubArray]
        indexOfRightSubArray += 1
        indexOfMergeSubArray += 1


def mergeSort(customList, leftIndex, rightIndex):
    if leftIndex < rightIndex:
        middleIndex = (leftIndex + (rightIndex - 1)) // 2
        mergeSort(customList, leftIndex, middleIndex)
        mergeSort(customList, middleIndex + 1, rightIndex)
        merge(customList, leftIndex, middleIndex, rightIndex)
    return customList


cList = [2, 1, 7, 6, 5, 3, 4, 9, 8]
print(mergeSort(cList, 0, 8))
