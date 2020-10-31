
def arrayCheck(arr, callBack):
    if len(arr) == 0:
        return False
    if not (callBack(arr[0])):
        return arrayCheck(arr[1:], callBack)

    return True


def isOdd(num):
    if num % 2 == 0:
        return False
    else:
        return True

def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(arrayCheck([1,2,3,4],isOdd))

print(arrayCheck([1,2,3,4],isEven))