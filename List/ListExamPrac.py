def firstSecond(givenList):
    # TODO
    givenList.sort(reverse=True)
    return givenList[0], givenList[1]


myList = [0, 3, 4, 1, 2, 5, 6, 7]
# myList.sort()
# print(myList)

print(firstSecond(myList))

newList = sorted(myList)
print(newList)
