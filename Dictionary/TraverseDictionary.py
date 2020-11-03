
#  Traverse through a dictionary
print('---- Traverse through a dictionary ----')


def traverseDictionary(Dict):
    for key in Dict:
        print(key, Dict[key])


myDiction = {"name": "Nirzhor", "age": 25, "address": "Barishal"}
traverseDictionary(myDiction)
