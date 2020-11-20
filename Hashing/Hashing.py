
def modNum(number, cellNumber):
    return number % cellNumber


def modASCII(string, cellNumber):
    total = 0
    for i in string:
        total += ord(i)
    return total % cellNumber


print(modNum(400, 24))
print(modASCII("ABC", 24))
