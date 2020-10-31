
def powerOfX(base, expo):

    if expo < 0 or not int(expo)==expo:
        return "Exponent must be positive integer number"

    if expo in [0]:
        return 1
    else:
        return base * powerOfX(base, expo - 1)

print(powerOfX(5,3))