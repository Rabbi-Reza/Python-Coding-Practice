
def GCD(a,b):

    if not int(a) == a or not int(b) == b:
        return "Input must be integer number"

    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b

    if b == 0:
        return a
    else:
        return GCD(b, a%b)


def GCD_2(a,b):

    if a == 1 or b == 1:
        return 1

    for i in range(2,a+1) and range(2,b+1):
        if a%i == 0 and b%i == 0:
            break

    return i


print(GCD(2,3))

print(GCD_2(3,5))