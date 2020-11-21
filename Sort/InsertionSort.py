
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
    print(customList)


cList = [2, 1, 7, 6, 5, 3, 4, 9, 8]
insertionSort(cList)
