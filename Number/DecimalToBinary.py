
def decimalToBinary(num):

    if num == 0:
        return 0
    else:
        return num % 2 + 10 * decimalToBinary(int(num/2))

print(decimalToBinary(-13))