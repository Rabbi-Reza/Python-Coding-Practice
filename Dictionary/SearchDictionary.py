#  Searching a dictionary
print('---- Searching a dictionary ----')


def searchInDictionaryByValue(Dict, value):
    for key in Dict:
        if Dict[key] == value:
            return key, Dict[key]
    return "Value not found"


def searchInDictionaryByKey(Dict, searchKey):
    for key in Dict:
        if key == searchKey:
            return key, Dict[key]
    return "Key not found"


myDiction = {"name": "Nirzhor", "age": 25, "address": "Barishal"}

value = 25
key = 'name'

print(searchInDictionaryByValue(myDiction, value))
print(searchInDictionaryByKey(myDiction, key))
