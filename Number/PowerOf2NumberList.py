from array import *

def powersOf2(n):

    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        prev = powersOf2(int(n/2))
        print(prev)
        curr = prev*2
        # arr.append(curr)

        return curr

# arr = array('i',[1])

num = 8650
print(powersOf2(num))

# print(arr)