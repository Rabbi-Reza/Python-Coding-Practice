
# Dictionary operations
EngToSpanish = {'one': 'uno', 'two': 'dos', 'three': 'tres', 'four': 'cuarto'}

print('-- in --- ')
print('one' in EngToSpanish)
print('uno' in EngToSpanish.values())

print('five' in EngToSpanish)
print('uno' in EngToSpanish)

print('-- for --- ')
for key in EngToSpanish:
    print(key)
    print(EngToSpanish[key])
    print(key, EngToSpanish[key])


# Python built in functions
print('-- all() --- ')
myDict = {1: True, 2: True}
print(all(myDict))
myDict = {11: 'True', 12: True}
print(all(myDict))
myDict = {21: 'True', 22: 'True'}
print(all(myDict))

myDict2 = {31: False, 32: False}
print(all(myDict2))

myDict3 = {0: False, 1: False, 3: True, 2: False}
print(all(myDict3))

myDict4 = {0: True, 2: False, 1: True, 3: True}
print(all(myDict4))

newDict = {}
print(all(newDict))

print('-- any() --- ')
myDict = {10: True, 20: True}
print(any(myDict))
myDict = {101: 'True', 102: True}
print(any(myDict))
myDict = {201: 'True', 202: 'True'}
print(any(myDict))

myDict20 = {0: False, 1: False}
print(any(myDict20))

myDict30 = {0: False, 1: False, 3: True, 2: False}
print(any(myDict30))

myDict40 = {0: True, 2: False, 1: True, 3: True}
print(any(myDict40))

newDict = {}
print(any(newDict))

print('-- len() --- ')
myDict40 = {0: True, 2: False, 1: True, 3: True}
print(len(myDict40))

# sorted method
print('-- sorted() --- ')
myDict = {'e': 1, 'a': 2, 'u': 3, 'o': 4, 'i': 5}

print(sorted(myDict))
print(sorted(myDict, reverse=True))

myDict2 = {'eooooa': 1, 'aas': 2, 'udd': 3, 'sseo': 4, 'werwi': 5}
print(sorted(myDict2, key=len))
print(sorted(myDict2, key=len, reverse=True))
