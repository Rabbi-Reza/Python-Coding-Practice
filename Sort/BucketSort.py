
import math


def insertionSort(customList):
    for i in range(1, len(customList)):
        # 2nd item
        key = customList[i]
        # 1st item
        j = i - 1
        while j >= 0 and key < customList[j]:
            customList[j+1] = customList[j]
            j -= 1
        customList[j+1] = key
    return customList


def bucketSort(customList):
    # Calculating bucket number and maximum of the List
    numberOfBuckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    arr = []
    # Creating buckets by creating 2D list
    for i in range(numberOfBuckets):
        arr.append([])
    # Inserting items in individual buckets
    for j in customList:
        index_bucket = math.ceil(j * numberOfBuckets / maxValue)
        arr[index_bucket - 1].append(j)
    # Sort the items in bucket
    for i in range(numberOfBuckets):
        arr[i] = insertionSort(arr[i])
    # Marging the buckets
    temp = 0
    for i in range(numberOfBuckets):
        for j in range(len(arr[i])):
            customList[temp] = arr[i][j]
            temp += 1

    return customList


cList = [2, 1, 7, 6, 5, 3, 4, 9, 8]
print(bucketSort(cList))
