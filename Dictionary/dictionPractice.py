
# How to create a Dictionary
print('---- How to create a Dictionary ----')

myDict1 = dict()
print(myDict1)

secondDict = {}
print(secondDict)

EngToSpanish = {"one": "uno", "two": "dos", "three": "tres"}
print(EngToSpanish)
print(EngToSpanish['two'])


# Dictionary methods
print('---- Dictionary methods ----')
myDiction = {"name": "Nirzhor", "age": 25, "address": "Barishal"}
myDict2 = myDiction.copy()
print(myDiction)
print(myDict2)

newDict = {}.fromkeys([2, 1, 3], 5)
print(newDict)
newDict2 = {}.fromkeys([2, 1, 3])
print(newDict2)

myDiction = {"name": "Nirzhor", "age": 25, "address": "Barishal"}
print(myDiction.get('age', 'Not found'))
print(myDiction.get('education', 'Not found in Dictionary'))
print(myDiction.get('education'))

print(myDiction.items())
tempDisplay = myDiction.items()
print(tempDisplay)

print(myDiction.keys())
tempDisplay = myDiction.keys()
print(tempDisplay)

print(myDiction.values())
tempDisplay = myDiction.values()
print(tempDisplay)

myDiction = {"name": "Nirzhor", "age": 25, "address": "Barishal"}
print(myDiction.setdefault('name', 'Rabbi'))
print(myDiction.setdefault('education', 'Bachelor'))
print(myDiction)
myDiction.setdefault('gender', 'Male')
print(myDiction)
