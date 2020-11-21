
def heapify(customList, numberOfElements, index):
    smallest = index
    leftIndex = index * 2
    rightIndex = index * 2 + 1

    if leftIndex < numberOfElements and customList[leftIndex] < customList[smallest]:
        smallest = leftIndex
    if rightIndex < numberOfElements and customList[rightIndex] < customList[smallest]:
        smallest = rightIndex

    if smallest is not index:  # !=
        customList[index], customList[smallest] = customList[smallest], customList[index]
        heapify(customList, numberOfElements, smallest)


def heapSort(customList):
    numberOfElements = len(customList)
    for index in range(int(numberOfElements / 2) - 1, -1, -1):
        heapify(customList, numberOfElements, index)

    for index in range(numberOfElements - 1, 0, -1):
        customList[index], customList[0] = customList[0], customList[index]
        heapify(customList, index, 0)
    customList.reverse()


cList = [2, 1, 8, 6, 5, 3, 4, 9, 7]
heapSort(cList)
print(cList)
