
#  Delete or remove a dictionary
print('---- Delete or remove a dictionary ----')

myDiction = {"name": "Nirzhor", "age": 25, "address": "Barishal"}
myDiction.pop('name')
print('pop => ', myDiction)
myDiction = {"name": "Nirzhor", "age": 25, "address": "Barishal"}
print(myDiction.pop('age'))
print('pop => ', myDiction)

print(myDiction.pop('city', 'City Not found'))
print(myDiction)

myDiction = {"name": "Nirzhor", "age": 25, "address": "Barishal"}
myDiction.popitem()  # Delete random key and value
print(myDiction)
myDiction = {"name": "Nirzhor", "age": 25, "address": "Barishal"}
print(myDiction.popitem())
print(myDiction)

myDiction = {"name": "Nirzhor", "age": 25, "address": "Barishal"}
myDiction.clear()
print(myDiction)
myDiction = {"name": "Nirzhor", "age": 25, "address": "Barishal"}
print(myDiction.clear())  # None
print(myDiction)

myDiction = {"name": "Nirzhor", "age": 25, "address": "Barishal"}
del myDiction['address']
print(myDiction)
myDiction = {"name": "Nirzhor", "age": 25, "address": "Barishal"}
del myDiction  # Removing whole Dictionary
# print(myDiction)
