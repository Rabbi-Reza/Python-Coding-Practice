#  Update / add an element to the dictionary
print('---- Update / add an element to the dictionary ----')

myDiction = {"name": "Nirzhor", "age": 25}
print(myDiction)

myDiction["age"] = 26
print(myDiction)

myDiction["address"] = "Barishal"
print(myDiction)

myDiction2 = {'A': 1, 'B': 2, 'C': 3}
myDiction.update(myDiction2)
print('update => ', myDiction)
