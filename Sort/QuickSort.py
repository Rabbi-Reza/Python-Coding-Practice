
def partition(customList, low, high):
    i = low - 1
    pivot = customList[high]
    for j in range(low, high):
        if customList[j] <= pivot:
            i += 1
            customList[i], customList[j] = customList[j], customList[i]
    customList[i + 1], customList[high] = customList[high], customList[i + 1]
    return (i + 1)


def quickSort(customList, low, high):
    if low < high:
        partitionIndex = partition(customList, low, high)
        quickSort(customList, low, partitionIndex - 1)
        quickSort(customList, partitionIndex + 1, high)
    # return customList


cList = [2, 1, 8, 6, 5, 3, 4, 9, 7]
# print(quickSort(cList, 0, 8))
quickSort(cList, 0, 8)
print(cList)
