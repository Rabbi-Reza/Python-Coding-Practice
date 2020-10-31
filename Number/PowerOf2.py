
def powerOfTwo(n):
    if n <= 0 and int(n) != n:
        return "\nInput is not integer or negative"
        # print("Input is not integer or negative")

    if n == 0:
        return 1
    else:
        return 2 * powerOfTwo(n-1)

print(powerOfTwo(-0.3))