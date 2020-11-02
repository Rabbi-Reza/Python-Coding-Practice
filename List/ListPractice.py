
shoppingList = ['Milk', 'Cheese', 'Butter']

print('Butter' in shoppingList)

# Accessing the list
print(shoppingList[1])
print(shoppingList[-1])

# Traversing the list
for i in shoppingList:
    print(i)

for i in range(len(shoppingList)):
    shoppingList[i] = "+-+ " + shoppingList[i] + " +-+"
    print(shoppingList[i])

empty = []
for i in empty:
    print("I am empty")

# Update/Insert - List
myList = [1, 2, 3, 4, 5, 6, 7]
print(myList)
myList[2] = 33
print(myList)

myList.insert(4, 15)
myList.insert(-2, 5)
print(myList)

myList.append(55)
print(myList)

myList = myList + [25]
print(myList)

newList = [11, 12, 13, 14]
myList.extend(newList)
print(myList)

# Slicing a list
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(letters[0:2])
print(letters[2:])
print(letters[:3])
print(letters[:])
print(letters[-1:-3])

letters[0:2] = ['x', 'y']
print(letters)

# Delete - List
letters.pop(2)
print(letters)

letters.pop()
print(letters)

print(letters.pop())
print(letters)

del letters[2]
print(letters)

del letters[1:3]
print(letters)

letters.remove('x')
print(letters)

#  Searching for an element in the List
myList = [10, 20, 30, 40, 50, 60, 70, 80, 90]

val = 50

if val in myList:
    print(myList.index(val))
else:
    print("Value not found")


def searchLinearInList(list, value):
    for i in list:
        if i == value:
            return list.index(value)

    return "Value not in list"


print(searchLinearInList(myList, val))

#  List operations
a = [1, 2, 3]
b = [4, 5, 6, 7]
print(a+b)

c = a+b
print(c)

A = [0, 1]
A = A * 4
print(A)

#  List functions
a = [0, 1, 2, 3, 4, 5, 6, 7]
print(len(a))
print(max(a))
print(min(a))
print(sum(a))
print(sum(a)/len(a))
print(sum(a)//len(a))

b = ['a', 'b', 'd', 'c', 'D']
print(max(b))
print(min(b))

sum = 0.0
count = 0.0
avg = 0.0

# while True:
#     inputValue = input("Enter a number : ")
#     if inputValue == "done":
#         if count == 0:
#             print("Nothing to calculate")
#         break

#     inputValue = float(inputValue)
#     sum = sum + inputValue
#     count = count + 1
#     avg = sum / count
# print("Average is : " + str(avg))

Avg = 0.0
avgList = []
while True:
    inputValue = input("Enter a number : ")
    if inputValue == "done":
        # if len(avgList) == 0:
        #     print("Nothing to calculate")
        break

    inpu = float(inputValue)
    avgList.append(inpu)
    print(avgList)
    # print(sum(avgList))
    print(len(avgList))

avg = sum(avgList) / len(avgList)
print("Average is : " + str(avg))

# numlist = list()
# while (True):
#     inp = input('Enter a number: ')
#     if inp == 'done':
#         break
#     value = float(inp)
#     numlist.append(value)

# average = sum(numlist) / len(numlist)
# print('Average:', average)

# Strings and Lists
name = 'Nirzhor'
listName = list(name)
print(listName)

name = 'My name is Nirzhor'
listName = name.split()
print(listName)
print(listName[2])

name = 'world-world1-world2-world3'

listName = name.split('rl')
print(listName)

delimiter = '-'
listName = name.split(delimiter)
print(listName)

print(delimiter.join(listName))
